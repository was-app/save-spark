from Persistence.repositories.client_repository import ClientRepository

class ClientService:
    def __init__(self):
        self.repo = ClientRepository()

    def create_client(self, user):
        return self.repo.create(client=user)

    def get_client(self, **filters):
        return self.repo.get(**filters)

    def update_balance(self, client_instance, amount):
        return self.repo.update(client_instance, current_balance=amount)
