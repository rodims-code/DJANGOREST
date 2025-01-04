from django import forms

from .models import Product

class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = ['name', 'content', 'price']