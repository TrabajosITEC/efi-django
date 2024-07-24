from django import forms    
from cars.models import Car
from cars.repositories.car import CarRepository
from locations.repositories.locality_repository import LocalityRepository
repo_car = CarRepository()
repo_loc = LocalityRepository()

from offer.models import Offer

class OfferForm(forms.ModelForm):
    cars = forms.ModelChoiceField(queryset=repo_car.get_all())
    location = forms.ModelChoiceField(queryset=repo_loc.get_all())

    class Meta:
        model = Offer
        fields = [
            "cars",
            "location",
            "price",
            "year"
        ]

        widgets = {
            "cars": forms.Select(),
            "location": forms.Select(),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "year": forms.NumberInput(attrs={"class": "form-control"}),
        }

# __all__ = (
#     "Media",
#     "MediaDefiningClass",
#     "Widget",
#     "TextInput",
#     "NumberInput",
#     "EmailInput",
#     "URLInput",
#     "PasswordInput",
#     "HiddenInput",
#     "MultipleHiddenInput",
#     "FileInput",
#     "ClearableFileInput",
#     "Textarea",
#     "DateInput",
#     "DateTimeInput",
#     "TimeInput",
#     "CheckboxInput",
#     "Select",
#     "NullBooleanSelect",
#     "SelectMultiple",
#     "RadioSelect",
#     "CheckboxSelectMultiple",
#     "MultiWidget",
#     "SplitDateTimeWidget",
#     "SplitHiddenDateTimeWidget",
#     "SelectDateWidget",
# )