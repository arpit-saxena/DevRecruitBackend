from django.urls import path
from . import views

urlpatterns = [
    path('add', views.addProduct, name='add_product'),
]
