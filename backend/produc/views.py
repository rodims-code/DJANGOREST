from django.http import JsonResponse
from .models import Product

from django.forms.models import model_to_dict

def api_view(request):
    # request != requests
    # request is a Django HttpRequest object
    query = Product.objects.all().order_by('?').first()
    data = {}
    if query:
        data = model_to_dict(query)
    return JsonResponse(data)