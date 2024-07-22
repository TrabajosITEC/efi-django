from django import forms

from payments.models import Payment

class PaymentsForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ["name"
                  ]
    
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control m-3','placeholder': 'Metodo de pago'}),
        }