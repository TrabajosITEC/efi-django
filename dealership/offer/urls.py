from django.urls import path

from offer.views.views_offers import (
    OfferList,
    OffertCreate,
    OffertDetail,
)
urlpatterns = [
    path(route = 'list/', view = OfferList.as_view(), name = 'listOffers'),
    path(route = 'create/', view = OffertCreate.as_view(), name = 'createOffers'),
    path(route = 'detail/<int:id>/detail/', view = OffertDetail.as_view(), name = 'DetailOffers'),
]

