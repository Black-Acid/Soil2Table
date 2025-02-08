from django.shortcuts import render
from supabase import Client, create_client
import os
from django.http import JsonResponse
from .serializers import ConsumerSignUPSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.utils import IntegrityError
import json
from rest_framework.views import APIView

from rest_framework.decorators import api_view


class ConsumerSignUP(APIView):
    def post(self, request):
        print(request.data)
        return Response("Message Recieved successfuly")








# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_KEY")
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) 


# @api_view()
# def home(request):
#     return Response({"message": "hello I am here successfully"})


# @api_view()
# def dummy_data(request):
#     data_input = supabase.table("Users Table").insert({
#         "username": "James Dzormeku",
#         "email": "something@gmail.com",
#         "Role": "Farmer",
#         "Phone_number": "0234231232",
#         "profile_picture": "ajshdlkjslajdkja",
#         "password_hash": "asjhdalksdasd",
#         "Address": "his address"
#     }).execute()
    
#     print(f"Insert response{data_input}")
    
    
#     response  = supabase.table("Users Table").select("*").execute()
#     print("Raw data from Supabase:", response, type(response))
#     if response.data:
#         data = response.data
#         serialized_object = NewSerializer(data, many=True)
        
#         return Response(serialized_object.data, status=status.HTTP_200_OK)
#     else:
#         return Response(
#         {"message": "No data found in the User table"},
#         status=status.HTTP_200_OK
#     )
    
#     # print("Raw data from Supabase:", response, type(response))
#     # print({"data": response.data})
#     # return JsonResponse({"data": str(response)})
    
#     # return Response(serialized_object)

# # Create your views here.
