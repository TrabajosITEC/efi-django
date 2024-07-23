from django.urls import path

from locations.views.country_views import (
    CountryList,
    CountryCreate,
    CountryUpdate,
    CountryDetail,
    CountryDelete

)

from locations.views.province_views import(
    ProvinceList,
    ProvinceCreate,
    ProvinceDetail,
    ProvinceDelete,
    ProvinceUpdate

)

urlpatterns = [
    # --- Rutas para Países --- #
    path(route = 'countries/', view = CountryList.as_view(), name = 'countries_list'),
    path(route = 'country_create/', view = CountryCreate.as_view(), name = 'country_create'),
    path(route = 'country_update/<int:id>/', view = CountryUpdate.as_view(), name = 'country_update'),
    path(route = 'country_detail/<int:id>/', view = CountryDetail.as_view(), name = 'country_detail'),
    path(route = 'country_delete/<int:id>/', view = CountryDelete.as_view(), name = 'country_delete'),

    # --- Rutas para Provincias --- #
    path(route = 'provinces/', view = ProvinceList.as_view(), name = 'provinces_list'),
    path(route = 'province_create/', view = ProvinceCreate.as_view(), name = 'province_create'),
    path(route = 'province_detail/<int:id>/', view = ProvinceDetail.as_view(), name = 'province_detail'),
    path(route = 'province_delete/<int:id>/', view = ProvinceDelete.as_view(), name = 'province_delete'),
    path(route = 'province_update/<int:id>/', view = ProvinceUpdate.as_view(), name = 'province_update'),

]