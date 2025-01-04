from django.http import JsonResponse
from .models import Product

from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_view(request):
    # request != requests
    # request is a Django HttpRequest object
    if request == "POST":
        return Response({'error': 'Invalid request'}, status=400)
    query = Product.objects.all().order_by('?').first()
    data = {}
    if query:
        data = model_to_dict(query)
        # serialization : mettre des donnees sur forme de dictionnaire
    return JsonResponse(data)