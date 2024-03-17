from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated
import requests as req
import http.client
import json
from urllib.parse import urlencode

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