from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from offer.views.views_offers import (
    OfferList,
    OfferCreate,
    OfferDetail,
)


urlpatterns = [
    path(route = 'list/', view = OfferList.as_view(), name = 'listOffers'),
    path(route = 'create/', view = OfferCreate.as_view(), name = 'createOffers'),
    path(route = 'detail/<int:id>/detail/', view = OfferDetail.as_view(), name = 'DetailOffers'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


