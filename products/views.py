from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory

from .models import Product, Category, Images
from .forms import ProductForm, CategoryForm, ImageForm

from django.utils.text import slugify

import hash_info

@login_required
def addProduct(request):
    ImageFormSet = modelformset_factory(
        Images,
        form=ImageForm,
        extra=5
    )

    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        formset = ImageFormSet(
            request.POST,
            request.FILES,
            queryset=Images.objects.none(),
        )
        if product_form.is_valid() and formset.is_valid():
            product = product_form.save(commit=False)
            product.added_by = request.user
            product.category = product_form.cleaned_data['category']
            product.slug = slugify(product_form.cleaned_data['name'])
            product.save()
            product.my_hash = hash_info.PRODUCT.encode(product.id)
            product.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Images(product=product, image=image)
                    photo.save()

            return redirect(product)
    else:
        product_form = ProductForm()
        formset = ImageFormSet(queryset=Images.objects.none())

    return render(
        request,
        'products/addproduct.html',
        {
            'product_form': product_form,
            'formset': formset,
        }
    )

def viewProduct(request, my_hash, slug):
    product_ids = hash_info.PRODUCT.decode(my_hash)

    if len(product_ids) != 1:
        raise Http404("Hash is wrong")
    product_id = product_ids[0]

    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product id corresponding to hash doesn't exist")
    
    if slug != product.slug:
        return redirect(product)

    return HttpResponse("YAY!")