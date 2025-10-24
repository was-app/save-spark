from Persistence.repositories.category_repository import CategoryRepository

class CategoryService:
    def __init__(self):
        self.repo = CategoryRepository()

    def get_all_categories(self):
        return self.repo.get_all()

    def get_category_by_name(self, name):
        return self.repo.get(name=name)
    
    def get_category_by_id(self, id):
        return self.repo.get(id=id)
    
    def create_category(self, name):
        pass

    def update_category(self, name):
        pass

    def delete_category(self, name):
        pass