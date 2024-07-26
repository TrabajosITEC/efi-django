from django.shortcuts import (
    render,
)

from django.views import View
from offer.forms import OfferImageForm
from offer.models import OfferImage

class OfferImageView(View):
    def get(self, request):
        form = OfferImageForm
        images = OfferImage.objects.all()
        return render(
            request,
            'offer_images/list.html',
            dict(
                images = images
            )
        )