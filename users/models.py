from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(blank=True, null=True, max_length=150)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    date_joined = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'phone_number',
        'username',
    ]
    USERNAME_FIELD = 'email'
