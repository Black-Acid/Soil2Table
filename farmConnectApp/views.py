from django.shortcuts import render
from supabase import Client, create_client
import os
from django.http import JsonResponse
from .serializers import NewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) 


@api_view()
def home(request):
    return Response({"message": "hello I am here successfully"})


@api_view()
def dummy_data(request):
    response  = supabase.table("User").select("*").execute()
    print("Raw data from Supabase:", response, type(response))
    if response.data:
        data = response.data
        serialized_object = NewSerializer(data, many=True)
        
        return Response(serialized_object.data, status=status.HTTP_200_OK)
    else:
        return Response(
            {"error": "Error fetching data from Supabase"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
    # print("Raw data from Supabase:", response, type(response))
    # print({"data": response.data})
    # return JsonResponse({"data": str(response)})
    
    # return Response(serialized_object)

# Create your views here.
