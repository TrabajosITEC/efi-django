from offer.models  import Offer
from typing import List, Optional
from cars.models import Car
from locations.models import Locality
from offer.models import Offer

class OfferRepository:
    def get_all(self) -> List[Offer]:
        return Offer.objects.all()
    
    def create(
            self,
            cars: Car,
            location: Locality,
            price: float,
    ) : return Offer.objects.create(
        cars=cars,
        location=location,
        price=price,
    )