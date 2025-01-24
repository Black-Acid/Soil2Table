from django.shortcuts import render
from supabase import Client, create_client
import os
from django.http import JsonResponse
from django.core.serializers import serialize


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY) 


def home(request):
    return JsonResponse({"message": "Hello My supabase is connected"})

def dummy_data(request):
    response  = supabase.table("User").select("*").execute()
    print("Raw data from Supabase:", response, type(response))
    print({"data": response.data})
    return JsonResponse({"data": str(response)})

# Create your views here.
