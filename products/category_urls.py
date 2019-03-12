from django.urls import path
from .views import ProductsByCategoryView, ViewAllCategories

urlpatterns = [
    path('all', ViewAllCategories, name="view_all_categories"),
    path('<my_hash>/<slug:slug>', ProductsByCategoryView.as_view(), name='view_category'),
]