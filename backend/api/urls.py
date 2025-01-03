from django.urls import path
from .views import api_view, acceuil

urlpatterns = [
    path('', api_view, name = 'api_view'),
    path('acceuil/', acceuil, name = 'acceuil'),
]