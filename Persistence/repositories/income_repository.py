from . import *

class IncomeTranscationRepository(BaseRepository):
    def __init__(self):
        super().__init__(IncomeTransaction)