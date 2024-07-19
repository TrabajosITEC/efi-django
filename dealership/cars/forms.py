from django import forms
from cars.models import (
    Brand,
    Car,
    CarModel,
    Category,
)

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = [
            'name'
        ]
    widgets = {
        'name': forms.TextInput()
    }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
        ]
    widgets = {
        'name': forms.TextInput()
    }

class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = [
            'name',
            'brand',
        ]
    widgets = {
        'name': forms.TextInput(),
        'brand': forms.Select(),
    }

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'car_model',
            'category',
        ]
    widgets = {
        'car_model': forms.Select(),
        'category': forms.Select(),
    }