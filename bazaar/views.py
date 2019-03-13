from django.views.generic import TemplateView
from products.models import Product
from django.db.models import Q

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()\
            .filter(approved=True)\
            .order_by('-time_added')
        return context

class AllProductsView(TemplateView):
    template_name = 'view_unmoderated_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()\
            .filter(Q(approved=True) | Q(reviewed_by_mod=False))\
            .order_by('-time_added')
        return context

class UnmoderatedProductsView(TemplateView):
    template_name = 'view_unmoderated_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()\
            .filter(reviewed_by_mod=False)\
            .order_by('time_added')
        return context
