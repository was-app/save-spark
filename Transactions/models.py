from django.db import transaction
from Persistence.services.client_service import ClientService
from Persistence.models import Client
from Persistence.services.transaction_service import TransactionService

class FinancialTransactionProcessor:
   
    def __init__(self):
        self.client_service = ClientService()
        self.transaction_service = TransactionService()

    def register_income(self, client, value, category, description=None, frequency=None):
        
        client_obj = self.client_service.get_client(client=client)
        
        income = self.transaction_service.register_income(
            client=client,
            value=value,
            category=category,
            description=description,
            frequency=frequency
        )

        new_balance = client_obj.current_balance + float(value)
        self.client_service.update_balance(client_obj, new_balance)
        return income

    def register_outgoing(self, client, value, category, description=None):

        client_obj = self.client_service.get_client(client=client)

        outgoing = self.transaction_service.register_outgoing(
            client=client,
            value=value,
            category=category,
            description=description
        )

        new_balance = client_obj.current_balance - float(value)
        self.client_service.update_balance(client_obj, new_balance)
        return outgoing

    def get_transactions(self, user):
        income_transactions = self.transaction_service.get_incomes_from_user(user)
        outgoing_transactions = self.transaction_service.get_outgoings_from_user(user)
        return income_transactions, outgoing_transactions

    def get_categories_by_id(self, id):
        return self.category_service.get_category_by_id(id)
    
    def get_categories_by_type(self, type_name):
        return self.transaction_service.get_category_by_type(type_name)

    def update_transaction_category(self, transaction_type, transaction_id, category):
        if transaction_type == 'income':
            transaction = self.transaction_service.get_income_by_id(transaction_id)
            if transaction:
                self.transaction_service.update_income(transaction, **{'category': category})
        else:
            transaction = self.transaction_service.get_outgoing_by_id(transaction_id)
            if transaction:
                self.transaction_service.update_outgoing(transaction, **{'category': category})
        return transaction
    
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
