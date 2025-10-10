from . import *
from utils.utils import detect_date_type

class OutgoingTranscationRepository(BaseRepository):
    def __init__(self):
        super().__init__(OutgoingTransaction)

    def get_outgoing_by_id(self, id):
        return self.model.objects.get(pk=id)
    
    def get_outgoings_from_user(self, user):
        return self.model.objects.filter(client=user)
    
    # By Day, Month or Year
    def get_outgoings_by_date(self, date):
        date_type = detect_date_type(date)
        filters = {}

        if date_type == "year":
            filters["carried_out_at__year"] = int(date)
        elif date_type == "month":
            year, month = map(int, date.split("-"))
            filters.update({"carried_out_at__year": year, "carried_out_at__month": month})
        elif date_type == "day":
            y, m, d = map(int, date.split("-"))
            filters["carried_out_at__date"] = date(y, m, d)

        return self.model.objects.filter(**filters)