from django.shortcuts import render, redirect
from payments.forms import PaymentsForm
from django.views import (
    View,
)
from payments.models import Payment
from payments.forms import PaymentsForm
from payments.repositories.paymente_repositorie import PaymentRepository

repo_payment = PaymentRepository()


class PaymentList(View):
    def get(self, request):
        payments = repo_payment.get_all()
        return render(request, "payments/list.html", dict(payments=payments))


class CreatePayment(View):
    def get(self, request):
        form = PaymentsForm()

        return render(request, "payments/create.html", dict(form=form))

    def post(self, request):
        form = PaymentsForm(request.POST)
        if form.is_valid():
            repo_payment.create(nombre=form.cleaned_data["name"])
            return redirect("listPayment")


class PaymentDelete(View):
    def get(self, request, id):
        payment = repo_payment.get_by_id(id=id)
        repo_payment.delete(payment=payment)
        return redirect("listPayment")


class PaymentUpdate(View):
    def get(self, request, id):
        payment = repo_payment.get_by_id(id=id)

        initial_data = {
            "name": payment.name,
        }
        form = PaymentsForm(initial=initial_data)
        return render(request, "payments/update.html", dict(form=form))

    def post(self, request, id):
        form = PaymentsForm(request.POST)
        if form.is_valid():
            repo_payment.update(
                payment=repo_payment.get_by_id(id=id),
                nombre=form.cleaned_data["name"],
            )

            return redirect("listPayment")