from Persistence.repositories.goal_repository import GoalRepository

class GoalService:
    def __init__(self):
        self.repo = GoalRepository()

    def create_goal(self, **kwargs):
        return self.repo.create(**kwargs)

    def update_goal(self, instance, **kwargs):
        return self.repo.update(instance, **kwargs)

    def delete_goal(self, instance):
        return self.repo.delete(instance)

    def get_goals_by_user(self, user):
        return self.repo.get_goals_by_user(user=user)

    def get_active_goals(self, user):
        return self.repo.get_active_goals(user=user)