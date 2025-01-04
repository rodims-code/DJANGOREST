import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

# Envois des donnees depuis un base de bonnes et renvois en json
#les ilite de django
def api_view(request, *args, **kwargs) :
    data = {
        'name': 'John',
        'age': 27,
        'language': 'python',
    }
    return JsonResponse(data) # return JSON