from django.shortcuts import render, redirect
from django.views import View
from offer.forms import OfferForm, OfferImageForm
from payments.forms import PaymentsForm
from offer.models import Offer, OfferGroup, OfferImage
from ..repositories.offer_repository import OfferRepository
repo_off = OfferRepository()
# Create your views here.

class OfferList(View):
    def get(self, request):
        # all_offers = repo_off.get_all()
        offer_groups = OfferGroup.objects.all()

        grouped_offers = {}
        for group in offer_groups:
            offers = Offer.objects.filter(offer_group=group)
            grouped_offers[group] = offers
        return render(
            request,
            "offers/list.html",
            dict(
                # offers = all_offers
                grouped_offers=grouped_offers    
            )
        )

class OffertCreate(View):
    def get(self, request):
        form = OfferForm()
        formPayments = PaymentsForm()
        formImage = OfferImageForm()

        return render(
            request,
            'offers/create.html',
            dict(
                form=form,
                formPayments=formPayments,
                formImage=formImage
            )
        )
    
    def post(self, request):
        form = OfferForm(request.POST)
        formPayments = PaymentsForm(request.POST)
        formImage = OfferImageForm(request.POST, request.FILES)
        if form.is_valid() and formImage.is_valid():
            # Crear la oferta
            new_offer = repo_off.create(
                cars=form.cleaned_data['cars'],
                location=form.cleaned_data['location'],
                price=form.cleaned_data['price'],
                year=form.cleaned_data['year'],
                seller=request.user
            )
            # Guardar la imagen relacionada con la oferta
            new_image = formImage.save(commit=False)
            new_image.offer = new_offer
            new_image.save()

            # Guardar las opciones de pago si el formulario de pagos es válido
            if formPayments.is_valid():
                for payment in formPayments.cleaned_data['payment_options']:
                    repo_off.create_payment(
                        offer=new_offer,
                        payment=payment
                    )
            return redirect('listOffers')
        else:
            return render(
                request,
                'offers/create.html',
                dict(
                    form=form,
                    formPayments=formPayments,
                    formImage=formImage
                )
            )   
        
class OffertDetail(View):
    def get(self, request, id):
        offer = repo_off.get_by_id(id)
        image = OfferImage.objects.filter(offer=offer)
        return render(
            request,
            'offers/detail.html',
            dict(
                offer=offer,image=image
            )
        )
