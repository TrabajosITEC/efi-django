from django.urls import path

from users.views import (
    RegisterView
)

urlpatterns = [
    # path('', index_view, name="index"), 
    # path('login/', view=LoginView.as_view(), name="login"),
    # path('logout/', view=LogoutView.as_view(), name="logout"),
    path(route='register/', view=RegisterView.as_view(), name='register')
]
