from Persistence.repositories.income_repository import IncomeTranscationRepository
from Persistence.repositories.outgoing_repository import OutgoingTranscationRepository

class TransactionService:
    def __init__(self):
        self.income_repo = IncomeTranscationRepository()
        self.outgoing_repo = OutgoingTranscationRepository()

    def register_income(self, user, amount, category):
        return self.income_repo.create(user=user, amount=amount, category=category)


    def registr_outgoing(self, user, amount, category):
        return self.outgoing_repo.create(user=user, amount=amount, category=category)
