from django.urls import path

from users.views import (
    RegisterView
)

urlpatterns = [
    path(route='register/', view=RegisterView.as_view(), name='register')
]
