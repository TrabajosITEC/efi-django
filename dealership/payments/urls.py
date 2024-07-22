from django.urls import path

from payments.views import (
    create_payment,
    payment_list,
    payment_delete,
    payment_update
)
urlpatterns = [
    path(route = 'create/', view = create_payment.as_view(), name = 'createPayment'),
    path(route = 'list/', view = payment_list.as_view(), name = 'listPayment'),
    path(route = '<int:id>/delete/', view = payment_delete.as_view(), name = 'DeletePayment'),
    path(route = '<int:id>/update/', view = payment_update.as_view(), name = 'UpdatePayment'),
]

