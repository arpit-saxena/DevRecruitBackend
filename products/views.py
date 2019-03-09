from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Product, Category
from .forms import ProductForm, CategoryForm

def viewCategories(request):
    return render(
        request,
        "products/view_categories.html",
        {'categories': Category.objects.all()},
    )

@login_required
def addProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            new_article = form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()

    return render(
        request,
        'templates/products/addproduct.html',
        {'form': form}
    )