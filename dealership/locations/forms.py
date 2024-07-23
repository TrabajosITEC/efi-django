from django import forms
from locations.models import(
    Country,
    Province,
    Locality

)

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country

        fields = [
            'name',

        ]

        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Nombre del País'})

        }

class ProvinceForm(forms.ModelForm):
    class Meta:
        model = Province

        fields = [
            'name',
            'country'

        ]

        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control'}),
            'country': forms.Select(attrs = {'class': 'form-control'})

        }

class LocalityForm(forms.ModelForm):
    class Meta:
        model = Locality

        fields = [
            'name',
            'province'

        ]

        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control'}),
            'province': forms.Select(attrs = {'class': 'form-control'})

        }
