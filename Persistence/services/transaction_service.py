from Persistence.repositories.income_repository import IncomeTranscationRepository
from Persistence.repositories.outgoing_repository import OutgoingTranscationRepository

class TransactionService:
    def __init__(self):
        self.income_repo = IncomeTranscationRepository()
        self.outgoing_repo = OutgoingTranscationRepository()

    def register_income(self):
        pass

    def registr_outgoing(self):
        pass