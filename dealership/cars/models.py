from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return  self.name
    
class CarModel(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(
        Brand,
        on_delete = models.CASCADE, 
        related_name = 'brands', #related name en plural
        null=False
    )
    def __str__(self):
        return  self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return  self.name
    
class Car(models.Model):
    car_model = models.ForeignKey(
        CarModel,
        on_delete = models.CASCADE, 
        related_name = 'car_models',
        null=False
    )
    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE, 
        related_name = 'categories',
        null=False
    )