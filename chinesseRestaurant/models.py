from django.db import models
from django.contrib.auth.models import User
import random


def create_new_ref_number():
    return str(random.randint(100000, 999999))

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=25)
    id = models.CharField(max_length=6, unique=True, primary_key=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=140, default='Product Description')
    objects = models.Manager()
    photo = models.ImageField(upload_to='images', null=True)

    class Meta:
        ordering = ('-name', )

    def __str__(self):
        """String for representing an item"""
        return f'{self.name} ({self.id})'


class Customer(models.Model):
    firstName = models.CharField(max_length=35)
    lastName = models.CharField(max_length=35)
    address = models.CharField(max_length=100)
    id = models.CharField(primary_key=True, max_length=8, unique=True)
    customer_phone = models.CharField(max_length=10)

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
