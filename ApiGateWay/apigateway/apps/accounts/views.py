from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import *
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.utils.decorators import method_decorator
from apps.core.serializers import LoginSerializer,AuthuserSerializer,AuthUser
from apps.core.utils import getSerializerErrorDetails
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(ensure_csrf_cookie, name='dispatch')
class LoginView(APIView) :
    permission_classes = (AllowAny,)

    def post(self,request):
        response = {"status": "success", "errorcode": "", "reason": "", "result": "", "httpstatus": HTTP_200_OK}
        try :
            data= request.data
            if LoginSerializer(data=data).is_valid():
                user = authenticate(request=request, username=data.get("username"), password=data.get("password"))
                
                if not user :
                    response['status'] = "error"
                    response['reason'] = "User does not exist."
                    response['httpstatus'] = HTTP_401_UNAUTHORIZED
                    return Response(response,status=response['httpstatus'])

                
                if  check_password(data.get("password"), user.password):
                    login(request,user)
                    refreshtoken =  RefreshToken.for_user(user)
                    response['status'] = "success"
                    response['httpstatus'] = HTTP_202_ACCEPTED
                    response['result'] = {
                        "refresh" : str(refreshtoken),
                        "access":str(refreshtoken.access_token)
                    }
                    return Response(response,status=response['httpstatus'])
                
                else :    
                    response['status'] = "error"
                    response['reason'] = "invalid credentials"
                    response['httpstatus'] = HTTP_401_UNAUTHORIZED
                    return Response(response,status=response['httpstatus'])

                
            else :
                response["status"] = "error"
                response["httpstatus"] = HTTP_400_BAD_REQUEST
                response["reason"] = f"Invalid message or body!"
                return Response(response,status=response['httpstatus'])         
           
        except Exception as e :
            response["status"] = "error"
            response["httpstatus"] = HTTP_500_INTERNAL_SERVER_ERROR
            response["reason"] = f"SomeThing went wrong!"

        return Response(response,status=response['httpstatus'] )

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView) :
    permission_classes = (AllowAny,)

    def post(self,request):
        response = {"status": "success", "errorcode": "", "reason": "", "result": "", "httpstatus": HTTP_200_OK}
        try :
            serializer =  AuthuserSerializer(data=request.data,partial=True)    
            try:   
                if serializer.is_valid(raise_exception=True):
                    serializer.save()              
                    response["httpstatus"] = HTTP_201_CREATED
                    response["result"] = f"user created successfully."
                    return Response(response,status=response['httpstatus'] )
      
            except ValidationError as e:
                response["status"] = "error"
                response["reason"] = f"{getSerializerErrorDetails(e)}"
                response["httpstatus"] = HTTP_406_NOT_ACCEPTABLE
                return Response(response,status=response['httpstatus'] )


        except Exception as e :
            response["status"] = "error"
            response["httpstatus"] = HTTP_500_INTERNAL_SERVER_ERROR
            response["reason"] = f"{e}"

        return Response(response,status=response['httpstatus'] )