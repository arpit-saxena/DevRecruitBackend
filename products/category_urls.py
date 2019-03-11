from django.urls import path
from .views import ProductsByCategoryView

urlpatterns = [
    path('<my_hash>/<slug:slug>/', ProductsByCategoryView.as_view(), name='view_category'),
]