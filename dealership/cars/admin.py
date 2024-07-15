from django.contrib import admin
from cars.models import (
    Brand,
    Car,
    CarModel,
    Category,
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'brand',
    )

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'car_model',
        'category',
    )