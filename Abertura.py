from datetime import datetime
from AberturaFechamento import AberturaFechamento
from AberturaFechamentoBase import AberturaFechamentoBase


class Abertura(AberturaFechamentoBase):
    def __init__(self, id_caixa, data_tempo: datetime):
        super(id_caixa, data_tempo)
        self.tipo = AberturaFechamento.ABERTURA