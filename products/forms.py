from django.forms import ModelForm, ImageField, ClearableFileInput
from .models import Category, Product, Images
from mptt.forms import TreeNodeChoiceField
from django import forms

class ProductForm(ModelForm):
    category = TreeNodeChoiceField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'negotiable',
        ]

class ImageForm(ModelForm):
    image = ImageField(label='Image', widget=ClearableFileInput)    
    class Meta:
        model = Images
        fields = ('image', )

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            'parent',
            'name',
            'description'
        ]

class ModReviewForm(forms.Form):
    approve = forms.BooleanField(label="Approve?", required=False)
    comments = forms.CharField(required=False)