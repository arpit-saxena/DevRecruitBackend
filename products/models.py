from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Category(models.Model):
    parent_id = models.ForeignKey(
        'self',
        models.CASCADE,
        blank=True,
        null=True,
    )
    name = models.CharField("Category name", max_length=50)
    description = models.TextField()

class Product(models.Model):
    name = models.TextField("Product name")
    description = models.TextField("Product description")
    time_added = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(
        'users.CustomUser',
        models.SET_NULL,
        null=True,
        blank=True,
        related_name='product_approved_by'
    )
    added_by = models.ForeignKey(
        'users.CustomUser',
        models.CASCADE,
        null=True,
        blank=True,
        related_name='product_added_by'
    )
    category = models.ForeignKey(
        'Category',
        models.SET_NULL,
        null=True
    )
    images = ArrayField(
        models.ImageField("Product Image"),
        size=5,
    )
    price = models.DecimalField(
        "Price of the product (in INR)",
        max_digits=8, #Max amount 9,99,999.99 (more than sufficient)
        decimal_places=2,
    )
    negotiable = models.BooleanField(default=False)
