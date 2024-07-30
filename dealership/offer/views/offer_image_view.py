from django.shortcuts import (
    render, redirect
)

from django.views import View
from offer.forms import OfferImageForm
from offer.models import OfferImage


class OfferImageView(View):
    def get(self, request):
        form = OfferImageForm()
        images = OfferImage.objects.all()
        return render(
            request,
            'offer_images/list.html',
            dict(
                form=form,
                images=images
            )
        )

    def post(self, request):
        form = OfferImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('offer_image_list')  
        images = OfferImage.objects.all()
        return render(
            request,
            'offer_images/list.html',
            dict(
                form=form,
                images=images
            )
        )
