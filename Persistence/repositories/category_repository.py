from . import *

class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Category)