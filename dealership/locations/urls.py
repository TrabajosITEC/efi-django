from django.urls import path

from locations.views.country_views import (
    CountryList,
    CountryCreate,
    CountryUpdate,
    CountryDetail,
    CountryDelete

)

urlpatterns = [
    path(route = 'countries_list/', view = CountryList.as_view(), name = 'countries_list'),
    path(route = 'country_create/', view = CountryCreate.as_view(), name = 'country_create'),
    path(route = 'country_update/<int:id>/', view = CountryUpdate.as_view(), name = 'country_update'),
    path(route = 'country_detail/<int:id>/', view = CountryDetail.as_view(), name = 'country_detail'),
    path(route = 'country_delete/<int:id>/', view = CountryDelete.as_view(), name = 'country_delete')

]