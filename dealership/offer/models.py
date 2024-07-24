from django.db import models
from cars.models import Car
from locations.models import Locality 

# Create your models here.

class Offer(models.Model):
    cars = models.ForeignKey(
        Car,
        on_delete=models.PROTECT,
        related_name='offer',
        null=False,
        help_text="Que auto desea vender?"
    )
    location = models.ForeignKey(
        Locality,
        on_delete=models.PROTECT,
        related_name="offer",
        null=False,
        help_text="Ciudad"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    year = models.IntegerField(
        default=0
    )

class OfferImage(models.Model):
    ...

class OfferPayment(models.Model):
    ...

