from django.shortcuts import render, redirect
from django.views import View
from offer.forms import OfferForm
from ..repositories.offer_repository import OfferRepository
repo_off = OfferRepository()
# Create your views here.

class OfferList(View):
    def get(self, request):
        all_offers = repo_off.get_all()
        return render(
            request,
            "offers/list.html",
            dict(
                offers = all_offers    
            )
        )

class OffertCreate(View):
    def get(self, request):
        form = OfferForm()

        return render(
            request,
            'offers/create.html',
            dict(
                form=form
            )
        )
    
    def post(self, request):
        form = OfferForm(request.POST)
        if form.is_valid():
            repo_off.create(
                cars=form.cleaned_data['cars'],
                location=form.cleaned_data['location'],
                price=form.cleaned_data['price']
            )
            return redirect('listOffers')