from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def api_view(request, *args, **kwargs) :
    data = {
        'name' : 'rodim\'s',
        'language' : 'python',
    }
    return JsonResponse(data)

def acceuil(request) :
    return render(request, 'acceuil.html')

def blog(request) :
    return render(request, 'blog.html')