from django import forms

from payments.models import Payment
from payments.repositories.paymente_repositorie import PaymentRepository
repo_pay = PaymentRepository()

class PaymentsForm(forms.ModelForm):
    payments = repo_pay.get_all()
    payment_options = forms.ModelMultipleChoiceField(
            label="Seleccione Opciones de Pago",
            queryset=payments,
            widget=forms.CheckboxSelectMultiple,
        )

    class Meta:
        model = Payment
        fields = ["payment_options"]
       