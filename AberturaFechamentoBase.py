from datetime import datetime
from AberturaFechamento import AberturaFechamento

class AberturaFechamentoBase():
    def __init__(self, id_caixa, data_tempo: datetime):
        self.id_caixa = id_caixa
        self.data_tempo = data_tempo
