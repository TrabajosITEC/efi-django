from django.urls import path

from offer.views.views_offers import (
    OfferList,
    OffertCreate,
    OffertDetail,
)

from offer.views.offer_image_view import OfferImageView

urlpatterns = [
    path(route = 'list/', view = OfferList.as_view(), name = 'listOffers'),
    path(route = 'create/', view = OffertCreate.as_view(), name = 'createOffers'),
    path(route = 'detail/<int:id>/detail/', view = OffertDetail.as_view(), name = 'DetailOffers'),
    path(route = 'offer_images/', view = OfferImageView.as_view(), name = 'offer_images')
]

