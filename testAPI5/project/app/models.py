from distutils.command.upload import upload
from email.policy import default
from enum import unique
from django.db import models
from django.utils.text import  slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True, blank=False)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=255, default='a')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='subcategories')
    image = models.ImageField(upload_to='subcategories/')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=255, default='a')
    subcategory = models.ForeignKey(SubCategory,
                                     on_delete=models.CASCADE,
                                     related_name='products')
    image_big = models.ImageField(upload_to='products/image_big/')
    image_medium = models.ImageField(upload_to='products/image_medium/')
    image_small = models.ImageField(upload_to='products/image_small/')
    price = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)

    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,
                             on_delete=models.CASCADE,
                             related_name='items')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                )
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity