from django.urls import path

from locations.views.country_views import (
    CountryList    

)

urlpatterns = [
    path(route = 'country_list/', view = CountryList.as_view(), name = 'country_list'),

]