from django.db import transaction
from Persistence.services.client_service import ClientService
from Persistence.services.transaction_service import TransactionService
from Persistence.services.category_service import CategoryService

class FinancialTransactionProcessor:
    def __init__(self):
        self.client_service = ClientService()
        self.transaction_service = TransactionService()
        self.category_service = CategoryService()

    def register_income(self, user, value, category, description=None, frequency=None):
        
        client = self.client_service.get_client(client=user)

        income = self.transaction_service.register_income(
            client=user,
            value=value,
            category=category,
            description=description,
            frequency=frequency
        )

        new_balance = client.current_balance + value
        self.client_service.update_balance(client, new_balance)
        return income

    def register_outgoing(self, user, value, category, description=None):

        client = self.client_service.get_client(client=user)
        outgoing = self.transaction_service.register_outgoing(
            client=user,
            value=value,
            category=category,
            description=description
        )

        new_balance = client.current_balance - value
        self.client_service.update_balance(client, new_balance)
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
    def delete_transaction(self, user, transaction_type, transaction_id):
        if transaction_type == 'income':
            transaction = self.transaction_service.get_income_by_id(transaction_id)
        else:
            transaction = self.transaction_service.get_outgoing_by_id(transaction_id)

        try:
            client = self.client_service.get_client(client=user)
        except Exception:
            raise ValueError("Client record not found for user")

        value = float(transaction.value or 0)

        if transaction_type == 'income':
            self.transaction_service.delete_income(transaction)
            new_balance = client.current_balance - value
        else:
            self.transaction_service.delete_outgoing(transaction)
            new_balance = client.current_balance + value

        self.client_service.update_balance(client, new_balance)

        return transaction