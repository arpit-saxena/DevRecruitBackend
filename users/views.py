from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse

from products.views import redirecter
import hash_info
from .models import CustomUser

def viewUser(request, my_hash, slug):
    user, need_to_redirect = redirecter(
        my_hash,
        slug,
        hash_info.USER,
        CustomUser
    )

    if need_to_redirect:
        return redirect(user, permanent=True)

    return HttpResponse("YAY!")
