from django.shortcuts import render
from .services import product_service
from django.http import JsonResponse

# Create your views here.
def hello_world(request):
    return JsonResponse({"message": "hello world"})