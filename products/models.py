from django.db import models
from django.contrib.postgres.fields import ArrayField
from mptt.models import MPTTModel, TreeForeignKey
from django.shortcuts import reverse
import hash_info

# Create your models here.
class Category(MPTTModel):
    name = models.CharField("Category name", max_length=50)
    description = models.TextField(blank=True, null=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='child_category_name',
    )
    my_hash = models.TextField(
        blank=True,
        null=True,
    )
    slug = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['id']

    def get_absolute_url(self):
        return reverse("view_category", kwargs={
            "slug": self.slug,
            "my_hash": self.my_hash,
        })

class Product(models.Model):
    name = models.TextField("Product name")
    description = models.TextField("Product description")
    time_added = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(
        'users.CustomUser',
        models.SET_NULL,
        null=True,
        blank=True,
        related_name='products_approved',
        limit_choices_to={'is_staff': True},
    )
    added_by = models.ForeignKey(
        'users.CustomUser',
        models.CASCADE,
        null=True,
        blank=True,
        related_name='products_added'
    )
    category = models.ForeignKey(
        'Category',
        models.SET_NULL,
        null=True,
        related_name='products'
    )
    price = models.DecimalField(
        "Price of the product (in INR)",
        max_digits=8, #Max amount 9,99,999.99 (more than sufficient)
        decimal_places=2,
    )   
    negotiable = models.BooleanField(default=False)
    my_hash = models.TextField(
        blank=True,
        null=True,
    )
    slug = models.TextField(
        blank=True,
    )

    def get_absolute_url(self):
        return reverse("view_product", kwargs={
            "slug": self.slug,
            "my_hash": self.my_hash,
        })

class Transaction(models.Model):
    seller = models.ForeignKey(
        'users.CustomUser',
        models.SET_NULL,
        related_name='products_sold',
        null=True,
    )
    buyer = models.ForeignKey(
        'users.CustomUser',
        models.SET_NULL,
        related_name='products_bought',
        null=True,
    )
    product = models.ForeignKey(
        'Product',
        models.PROTECT
    )
    time = models.DateTimeField(
        'Time of transaction',
        auto_now_add=True
    )

#Helper class to store images
class Images(models.Model):
    product = models.ForeignKey(
        Product,
        models.CASCADE,
        default=None,
        related_name='product_image',
    )

    image = models.ImageField(
        upload_to='uploads/',
        verbose_name='Image',
    )