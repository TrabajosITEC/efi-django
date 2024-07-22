from django.urls import path

from payments.views import (
    CreatePayment,
    PaymentList,
    PaymentDelete,
    PaymentUpdate
)
urlpatterns = [
    path(route = 'create/', view = CreatePayment.as_view(), name = 'createPayment'),
    path(route = 'list/', view = PaymentList.as_view(), name = 'listPayment'),
    path(route = '<int:id>/delete/', view = PaymentDelete.as_view(), name = 'DeletePayment'),
    path(route = '<int:id>/update/', view = PaymentUpdate.as_view(), name = 'UpdatePayment'),
]

