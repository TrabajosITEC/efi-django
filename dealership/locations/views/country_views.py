from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    redirect, 
    render
    
)

from django.utils.decorators import method_decorator
from django.views import View
from locations.forms import CountryForm
from locations.models import Country
from locations.repositories.country_repository import CountryRepository

country_repository = CountryRepository()

class CountryList(View):
    def get(self, request):
        all_countries = country_repository.get_all()

        return render(
            request,
            'country/list.html',
            dict(
                countries = all_countries

            )

        )
