from . import *

class GoalRepository(BaseRepository):
    def __init__(self):
        super().__init__(Goal)

    # You can also add custom methods:
    def get_goals_by_user(self, user):
        return self.model.objects.filter(client=user)
    
    def get_active_goals(self, user):
        return self.model.objects.filter(client=user, current_amount__lt=models.F('target_amount'))
        