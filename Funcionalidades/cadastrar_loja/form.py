# cadastrar_loja/forms.py
from django import forms
from .models import Store, Product

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name', 'description', 'logo')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity', 'image', 'active')
