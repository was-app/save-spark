from . import *

class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Category)
    
    def get_all(self):
        return self.model.objects.all().order_by('name')

    # def get_category_id(self, category):