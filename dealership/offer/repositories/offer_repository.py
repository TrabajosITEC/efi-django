from offer.models  import Offer
from typing import List, Optional

class OfferRepository:
    def get_all(self) -> List[Offer]:
        return Offer.objects.all()
    