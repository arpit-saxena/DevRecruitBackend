from django.urls import path
from .views import viewCategory

urlpatterns = [
    path('<my_hash>/<slug:slug>/', viewCategory, name='view_category'),
]