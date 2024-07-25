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
            year: int,):
        offer = Offer(
            cars=cars,
            location=location,
            price=price,
            year=year,)
        offer.save() # La clave esta en aca hacer un save y no crear el objeto en la base de datos. Eso lo hago con el super despues de haber agregado "GroupOfert"
        return offer 
        