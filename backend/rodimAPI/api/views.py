from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def api_view(request, *args, **kwargs):
    data = {
        'name': 'Rodim',
        'age': 26,
        'language': 'Python'
    }
    return JsonResponse(data)
