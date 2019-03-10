from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.shortcuts import reverse

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(blank=True, null=True, max_length=150)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    date_joined = models.DateTimeField(auto_now_add=True)
    my_hash = models.TextField(
        blank=True,
        null=True,
    )
    slug = models.TextField(
        blank=True,
    )

    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'phone_number',
        'username',
    ]
    USERNAME_FIELD = 'email'

    def get_absolute_url(self):
        return reverse("view_user", kwargs={
            "slug": self.slug,
            "my_hash": self.my_hash
        })

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)
