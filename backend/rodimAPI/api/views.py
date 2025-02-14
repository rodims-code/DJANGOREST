import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def api_view(request, *args, **kwargs):
    data = {
        'name': 'Rodim',
        'age': 26,
        'language': 'Python'
    }
    print(request.body)
    data = json.loads(request.body) #byte string
    print(data)
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    data['post_data'] = dict(request.POST)
    print(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
