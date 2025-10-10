from Persistence.repositories.income_repository import IncomeTranscationRepository
from Persistence.repositories.outgoing_repository import OutgoingTranscationRepository

class TransactionService:
    def __init__(self):
        self.income_repo = IncomeTranscationRepository()
        self.outgoing_repo = OutgoingTranscationRepository()

    # Mandar client (request.user), value, category
    def register_income(self, **kwargs):
        self.income_repo.create(**kwargs)

    def update_income(self, **kwargs):
        self.income_repo.update(**kwargs)

    def delete_income(self, **kwargs):
        self.income_repo.delete(**kwargs)

    def register_outgoing(self, **kwargs):
        self.outgoing_repo.create(**kwargs)

    def update_outgoing(self, **kwargs):
        self.income_repo.update(**kwargs)

    def delete_outgoing(self, **kwargs):
        self.income_repo.delete(**kwargs)
    
    def get_income_by_id(self, id):
        return self.income_repo.get_income_by_id(id=id)

    def get_incomes_from_user(self, user):
        return self.income_repo.get_incomes_from_user(user=user)

    def get_incomes_by_date(self, date):
        return self.income_repo.get_incomes_by_date(date=date)

    def get_outgoing_by_id(self, id):
        return self.outgoing_repo.get_outgoing_by_id(id=id)

    def get_outgoings_from_user(self, user):
        return self.outgoing_repo.get_outgoings_from_user(user=user)
    
    def get_outgoings_by_date(self, date):
        return self.outgoing_repo.get_outgoings_by_date(date=date)