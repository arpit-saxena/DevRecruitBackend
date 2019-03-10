from django.urls import path
from . import views
from django.shortcuts import reverse

urlpatterns = [
    path('<my_hash>/<slug:slug>/', views.viewUser, name='view_user')
]
