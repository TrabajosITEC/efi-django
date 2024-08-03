from django.shortcuts import render, redirect
from django.views import View
from offer.forms import OfferForm
from payments.forms import PaymentsForm
from offer.models import Offer, OfferGroup, OfferImage
from ..repositories.offer_repository import OfferRepository
repo_off = OfferRepository()

class OfferList(View):
    def get(self, request):

        offer_groups = OfferGroup.objects.all()

        grouped_offers = {}
        for group in offer_groups:
            offers = Offer.objects.filter(offer_group=group)
            grouped_offers[group] = offers
        return render(
            request,
            "offers/list.html",
            dict(
            
                grouped_offers=grouped_offers    
            )
        )
class OfferCreate(View):
    def get(self, request):
        form = OfferForm()
        formPayments = PaymentsForm()

        return render(
            request,
            'offers/create.html',
            dict(
                form=form,
                formPayments=formPayments
            )
        )
    
    def post(self, request):
        form = OfferForm(request.POST)
        formPayments = PaymentsForm(request.POST)
        if form.is_valid():
       
            new_offer = repo_off.create(
                cars=form.cleaned_data['cars'],
                location=form.cleaned_data['location'],
                price=form.cleaned_data['price'],
                year=form.cleaned_data['year'],
                seller=request.user
            )

            if formPayments.is_valid():
                for payment in formPayments.cleaned_data['payment_options']:
                    repo_off.create_payment(
                        offer=new_offer,
                        payment=payment
                    )
            
            images = request.FILES.getlist('images')  
            descriptions = request.POST.getlist('descriptions')  

            for i, image in enumerate(images):
                description = descriptions[i] if i < len(descriptions) else ''  
                OfferImage.objects.create(
                    offer=new_offer,
                    image=image,
                    description=description
                )

            return redirect('listOffers')
        else:
            return render(
                request,
                'offers/create.html',
                dict(
                    form=form,
                    formPayments=formPayments
                )
            )

class OfferDetail(View):
    def get(self, request, id):
        offer = repo_off.get_by_id(id)
        images = OfferImage.objects.filter(offer=offer)
        return render(
            request,
            'offers/detail.html',
            dict(
                offer=offer,
                image=images
            )
        )
