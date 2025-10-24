from Persistence.repositories.income_repository import IncomeTranscationRepository
from Persistence.repositories.outgoing_repository import OutgoingTranscationRepository
from Persistence.repositories.category_repository import CategoryRepository

class TransactionService:
    def __init__(self):
        self.income_repo = IncomeTranscationRepository()
        self.outgoing_repo = OutgoingTranscationRepository()
        self.category_repo = CategoryRepository()

    # Mandar client (request.user), value, category
    def register_income(self, **kwargs):
        self.income_repo.create(**kwargs)

    def update_income(self, instance, **kwargs):
        self.income_repo.update(instance, **kwargs)

    def delete_income(self, instance):
        self.income_repo.delete(instance)

    def register_outgoing(self, **kwargs):
        self.outgoing_repo.create(**kwargs)

    def update_outgoing(self, instance, **kwargs):
        self.outgoing_repo.update(instance, **kwargs)

    def delete_outgoing(self, instance):
        self.outgoing_repo.delete(instance)
    
    def get_income_by_id(self, id):
        return self.income_repo.get_income_by_id(id=id)

    def get_incomes_from_user(self, user):
        return self.income_repo.get_incomes_from_user(user=user)

    def get_incomes_by_date(self, date):
        return self.income_repo.get_incomes_by_date(date=date)
    
    def get_incomes_by_category(self, category):
        return self.income_repo.get_incomes_by_category(category=category)

    def get_outgoing_by_id(self, id):
        return self.outgoing_repo.get_outgoing_by_id(id=id)

    def get_outgoings_from_user(self, user):
        return self.outgoing_repo.get_outgoings_from_user(user=user)
    
    def get_outgoings_by_date(self, date):
        return self.outgoing_repo.get_outgoings_by_date(date=date)
    
    def get_outgoings_by_category(self, category):
        return self.outgoing_repo.get_outgoings_by_category(category=category)
    
    def get_all_categories(self):
        return self.category_repo.get_all()
    
    def get_category_by_type(self, type):
        return self.category_repo.filter(type=type)