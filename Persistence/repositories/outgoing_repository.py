from . import *

class OutgoingTranscationRepository(BaseRepository):
    def __init__(self):
        super().__init__(OutgoingTransaction)