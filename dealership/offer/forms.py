from django import forms    
from ..cars.models import Car

from offer.models import Offer

class OfferForm(forms.ModelForm):
    cars = forms.ModelChoiceField(queryset=Car.objects.all())

    class Meta:
        model = Offer
        fields = [
            "cars",
            "location",
            "price"
        ]
        widgets = {
            "cars": forms.Select()
        }
#   widgets = {
#             "name": forms.TextInput(attrs={'class': 'form-control m-3','placeholder': 'Metodo de pago'}),
#         }
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