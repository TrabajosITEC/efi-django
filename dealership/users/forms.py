from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile

class UserRegisterForm(UserCreationForm):
    SELLER_CHOICES = [
        (True, 'Sí'),
        (False, 'No'),
    ]
    is_seller = forms.ChoiceField(choices=SELLER_CHOICES, help_text="Campo Requerido")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control custom-class'}),
            'email': forms.EmailInput(attrs={'class': 'form-control custom-class', 'required':'required'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control custom-class'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control custom-class'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control custom-class', 'required':'required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control custom-class', 'required':'required'}),
            'is_seller': forms.Select(attrs={'class': 'form-control custom-class'}),
        }

    def save(self, commit=True):
            user = super().save(commit=False)
            if commit:
                user.save()
                profile = user.profile
                profile.is_seller = self.cleaned_data['is_seller']
                profile.save()
            return user