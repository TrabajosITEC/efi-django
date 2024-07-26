from django.db import models
from cars.models import Car
from locations.models import Locality 
from django.contrib.auth.models import User


# Create your models here.
class OfferGroup(models.Model):
    cars = models.ForeignKey(
        Car,
        on_delete=models.PROTECT,
        related_name='offer_groups',
        null=False
    )
    location = models.ForeignKey(
        Locality,
        on_delete=models.PROTECT,
        related_name='offer_groups',
        null=False
    )

    class Meta:
        unique_together = ('cars', 'location')

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
    offer_group = models.ForeignKey(
        OfferGroup,
        on_delete=models.PROTECT,
        related_name='offer',
        null=False
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='offer',
        null=False
    )

    def save(self, *args, **kwargs):
        # Obtener o crear el grupo de ofertas correspondiente
        offer_group, created = OfferGroup.objects.get_or_create(
            cars=self.cars,
            location=self.location
        )
        self.offer_group = offer_group

        super().save(*args, **kwargs)

class OfferImage(models.Model):
    ...

class OfferPayment(models.Model):
    ...

