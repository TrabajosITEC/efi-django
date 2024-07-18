from django.urls import path

from home.views import (
        RegisterView,
        IndexView

    )

urlpatterns = [
    path(route = '', view = IndexView.as_view(), name = 'index'),
    path(route = 'register', view = RegisterView.as_view(), name = 'register')

]