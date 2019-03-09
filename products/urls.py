from django.urls import path
from . import views

urlpatterns = [
    path('add', views.addProduct, name='add_product'),
    path('<my_hash>/<slug:slug>/', views.viewProduct,
    name='view_product')
]
