from datetime import datetime
from Venda import Venda

class Caixa:
    def __init__(self):
        self.id_funcionario_atual = None
        self.lista_vendas: list[Venda] = []
        self.lista_abertura_fechamento:list[datetime] = []