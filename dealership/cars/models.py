from django.db import models
from brands.models import Brand
from car_models.models import CarModel
from categories.models import Category

class Car(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel,on_delete=models.CASCADE)
    year = models.IntegerField()
    price = models.DecimalField()

    def __str__(self):
        return f'{self.brand.name} {self.car_model.name} ({self.year})'