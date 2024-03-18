from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated
import requests as req
import http.client,json
import pandas as pd
from urllib.parse import urlencode
from rest_framework.decorators import api_view
# from .producer import publish


# Create your views here.
class InventoryView(APIView):
    permission_classes =(IsAuthenticated,)

    def __init__(self) :
        self.__conn =  http.client.HTTPConnection("localhost", port=8001)

    def get(self,request):       
        query_string = urlencode(request.query_params)
      
        self.__conn.request("GET", url=f"{str(request.path)}?{query_string}")
        r1 = self.__conn.getresponse()         
        response = json.loads(r1.read().decode())  
        return Response(response,status=r1.status)     

    def post(self,request):        
        self.__conn.request("POST", str(request.path),body=json.dumps(request.data))
        r1 = self.__conn.getresponse()         
        response = json.loads(r1.read().decode())  
        return Response(response,status=r1.status)

    def patch(self,request,id):        
        self.__conn.request("PATCH", str(request.path),body=json.dumps(request.data))
        r1 = self.__conn.getresponse()         
        response = json.loads(r1.read().decode())  
        return Response(response,status=r1.status)

    def delete(self,request,id):        
        self.__conn.request("DELETE", str(request.path))
        r1 = self.__conn.getresponse()         
        response = json.loads(r1.read().decode())  
        return Response(response,status=r1.status)
    
 

class UploadView(APIView):
    def __init__(self) :
        self.__conn =  http.client.HTTPConnection("localhost", port=8001)
    
    def post(self,request) :
        response = {"status": "success", "errorcode": "", "reason": "", "result": "File uploading successfull", "httpstatus": HTTP_200_OK}
        data = request.data  
        file_data = data['file']
        allowed_extensions = ['csv', 'CSV']
        ext = str(file_data).lower().split('.')[-1]
                
        if len(file_data) <= 0 :
            raise Exception("please select file first!!")
        elif ext not in allowed_extensions:
            raise Exception( "Only CSV files are allowed.")

        df = pd.read_csv(file_data)
        # publish('books',df.to_dict('records'))        
        return Response(response,status=response.get("httpstatus"))
    