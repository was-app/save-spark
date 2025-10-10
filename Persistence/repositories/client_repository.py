from . import *

class ClientRepository(BaseRepository):
    def __init__(self):
        super().__init__(Client)

    # You can also add custom methods:
    def get_by_user(self, user):
        return self.model.objects.filter(client=user)

    def increase_balance(self, instance, amount):
        instance.current_balance += amount
        instance.save()
        return instance
    
    def get_user_by_id(self, id):
        return self.model.objects.get(pk=id)
