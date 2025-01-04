import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def api_view(request, *args, **kwargs) :
    # request => HttpRequest
    print (request.body)
    data = json.loads(request.body)
    print (data)
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    data['post-data']= dict(request.POST)
    print (request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data) # return JSON