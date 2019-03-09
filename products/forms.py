from django.forms import ModelForm
from .models import Category, Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'category',
            'images',
            'price',
            'negotiable',
        ]

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            'parent',
            'name',
            'description'
        ]