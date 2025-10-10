from django.db import transaction
from Persistence.services.client_service import ClientService
from Persistence.services.transaction_service import TransactionService

class FinancialTransactionProcessor:
   
    def __init__(self):
        self.client_service = ClientService()
        self.transaction_service = TransactionService()

    @transaction.atomic
    def process_transaction(self, user, income=0, expense=0,
                            income_category=None, expense_category=None,
                            action="register"):


        try:
            client = self.client_service.get_client(client=user)
        except:
            client = self.client_service.create_client(user)

        result = {}

        if action == "register":
            if expense > income:
                expense = income

            if income > 0 and income_category:
                self.transaction_service.register_income(user, income, income_category)

            if expense > 0 and expense_category:
                self.transaction_service.register_outgoing(user, expense, expense_category)

            new_balance = client.current_balance + income - expense
            self.client_service.update_balance(client, new_balance)

            result["status"] = "registered"
            result["current_balance"] = new_balance

        elif action == "simulate":
            result["balance"] = income - expense
            result["description"] = "Simulation"

        else:
            raise ValueError("Invalid action")

        return result
