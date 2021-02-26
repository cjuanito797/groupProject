from django.db import models
from django.contrib.auth.models import User
import random

from django.urls import reverse


def create_new_ref_number():
    return str(random.randint(100000, 999999))


class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True,
                            default='someValue')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chinesseRestaurant:item_list',
                       args=[self.slug])


class Item(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='items',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, default='someValue')
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chinesseRestaurant:item_list',
                       args=[self.id, self.slug])


class Customer(models.Model):
    firstName = models.CharField(max_length=35)
    lastName = models.CharField(max_length=35)
    address = models.CharField(max_length=100)
    id = models.CharField(
        primary_key=True,
        max_length=6,
        blank=True,
        editable=False,
        unique=True,
        default=create_new_ref_number()
    )
    customer_phone = models.CharField(max_length=10)
    email = models.EmailField(default='someEmail')

    def __str__(self):
        """String for representing the customer"""
        return f'{self.firstName} {self.lastName} ({self.id})'


class Order(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=6,
        blank=True,
        editable=False,
        unique=True,
        default=create_new_ref_number()
    )
    orderQty = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now=True)
    deliveryChoices = (
        ('delivery', 'Delivery'),
        ('pickup', 'Pickup')
    )

    deliveryPref = models.CharField(max_length=10,
                                    choices=deliveryChoices,
                                    default='pickup')

    customer = models.ForeignKey('Customer',
                                 on_delete=models.CASCADE,
                                 related_name='orders')

    def __str__(self):
        """String representation for an order object"""
        return f'{self.customer.firstName}, {self.customer.lastName}, {self.customer.customer_phone}, ' \
               f'{self.id}'
