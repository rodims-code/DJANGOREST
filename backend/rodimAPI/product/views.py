from .models import Product
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
def api_view(request):
    #request != requests
    #request is a Django object, requests is a Python module
    query = Product.objects.all().order_by('?').first()
    data = {}
    if query:
        #data['name'] = query.name
        #data['description'] = query.description
        #data['price'] = query.price
        data = model_to_dict(query)
        #serislization : convserion of complex data types to a format that can be stored or transmitted and reconstructed later
    return JsonResponse(data)