from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.views.generic.detail import DetailView
from django.views.generic import ListView

from .models import Product, Category, Images
from .forms import ProductForm, CategoryForm, ImageForm, ModReviewForm

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

def redirecter(my_hash, slug, hasher, my_class):
    object_ids = hasher.decode(my_hash)

    if len(object_ids) != 1:
        raise Http404("Hash is wrong")
    object_id = object_ids[0]

    try:
        obj = my_class.objects.get(pk=object_id)
    except my_class.DoesNotExist:
        raise Http404("id corresponding to hash doesn't exist")
    
    if slug != obj.slug:
        return obj, True
    return obj, False

class viewProductClass(DetailView):
    model = Product
    template_name = 'products/viewproduct.html'

    def get_object(self):
        product = self.kwargs.get('product')
        if product:
            return product
        
        return super().get_object(self)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_qset'] = self.kwargs.get('category_qset')
        context['form'] = self.kwargs.get('form')
        return context
    
def viewProduct(request, my_hash, slug):
    product, need_to_redirect = redirecter(
        my_hash,
        slug,
        hash_info.PRODUCT,
        Product
    )

    if request.method == 'POST' and request.user.groups.filter(name='Moderators').exists():
        form = ModReviewForm(request.POST)
        if form.is_valid():
            product.approved = form.cleaned_data['approve']
            product.mod_review = form.cleaned_data['comments']
            product.reviewed_by_mod = True
            if form.cleaned_data['approve']:
                product.approved_by = request.user
            product.save()
            return redirect(product)
    elif request.method == 'GET':
        form = ModReviewForm()

    if need_to_redirect:
        return redirect(product, permanent=True)

    return viewProductClass.as_view()(request, product=product,
    category_qset=product.category.get_ancestors(), form=form)

class ProductsByCategoryView(ListView):
    template_name = 'products/view_products_by_category.html'
    queryset = Product.objects.all()
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_qset'] = self.category.get_ancestors(include_self=True)
        return context

    def get_queryset(self):
        category, need_to_redirect = redirecter(
            self.kwargs['my_hash'],
            self.kwargs['slug'],
            hash_info.CATEGORY,
            Category
        )

        if need_to_redirect:
            return redirect(category, permanent=True)

        category_queryset = category.get_descendants(include_self=True)
        self.queryset = Product.objects.all().filter(
            category__in=category_queryset
        )
        self.category = category
        print('yay')
        return self.queryset
