from . import *
from Persistence.repositories.utils.utils import detect_date_type

class IncomeTranscationRepository(BaseRepository):
    def __init__(self):
        super().__init__(IncomeTransaction)

    def get_income_by_id(self, id):
        return self.model.objects.get(pk=id)
    
    def get_incomes_from_user(self, user):
        return self.model.objects.filter(client=user)
    
    # By Day, Month or Year
    def get_incomes_by_date(self, date):
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
