from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated
from .serializers import BooksSerializer,Books
import json


# Create your views here.
class InventoryView(APIView):

    def get(self,request):
        response = {"status": "success", "errorcode": "", "reason": "", "result": "", "httpstatus": HTTP_200_OK}
        try:
            print(request.query_params)   
            query = request.query_params
            title = query.get("title",None)
            author = query.get("author",None)
            isbn = query.get("isbn",None)
            
            if not title and author and isbn :
                queryset = Books.objects.all()
            if title :
                queryset = Books.objects.filter(title=title).all()
            if author :
                queryset = Books.objects.filter(authors=author).all()
            if isbn :
                queryset = Books.objects.filter(isbn=isbn).all()
            if title and author and isbn :
                queryset = Books.objects.filter(title=title,authors=author,isbn=isbn).all()            
            queryset = Books.objects.all()
            serializer = BooksSerializer(queryset,many=True)
            response["result"] =serializer.data
        except Exception as e:
            print(e)

        return Response(response,status=response.get("httpstatus"))  

    def post(self,request):
        response = {"status": "success", "errorcode": "", "reason": "", "result": "", "httpstatus": HTTP_200_OK}
        try:
            data = json.loads(request.body)
            serializer = BooksSerializer(data=data,partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()                
                response["result"] = serializer.data
                return Response(response,status=response.get("httpstatus"))
        except Exception as e:
            response["status"] = "error"
            response["httpstatus"] = HTTP_500_INTERNAL_SERVER_ERROR
            response["reason"] = f"{e}"
        return Response(response,status=response.get("httpstatus")) 

    def patch(self,request,id):
        response = {"status": "success", "errorcode": "", "reason": "", "result": "", "httpstatus": HTTP_200_OK}
        try:
           
            data = json.loads(request.body)     
            try:     
                queryset = Books.objects.get(id=id)
            except Books.DoesNotExist as e :
                response["status"] = "error"
                response["httpstatus"] = HTTP_404_NOT_FOUND
                response["reason"] = f"{e}"
                return Response(response,status=response.get("httpstatus"))


            serializer = BooksSerializer(queryset, data=data,partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()         
            response["result"] = serializer.data
            return Response(response,status=response.get("httpstatus"))
        
        except Exception as e:
            response["status"] = "error"
            response["httpstatus"] = HTTP_500_INTERNAL_SERVER_ERROR
            response["reason"] = f"{e}"
        return Response(response,status=response.get("httpstatus"))


    def delete(self,request,id):
        response = {"status": "success", "errorcode": "", "reason": "", "result": "", "httpstatus": HTTP_200_OK}
        try:         
            
            Books.objects.get(id=id).delete()                 
            response["result"] = "deleted successfully"
            return Response(response,status=response.get("httpstatus"))
        
        except Exception as e:
            response["status"] = "error"
            response["httpstatus"] = HTTP_500_INTERNAL_SERVER_ERROR
            response["reason"] = f"{e}"
        return Response(response,status=response.get("httpstatus"))