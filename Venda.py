from datetime import datetime
from Produto import Produto


class Venda:
    def __init__(self, id_cliente, id_funcionario, id_caixa, lista_produtos: list[Produto], data_tempo: datetime = datetime.now().strftime("%d/%m/%Y")):
        self.id_cliente = id_cliente
        self.id_funcionario = id_funcionario
        self.id_caixa = id_caixa
        self.lista_produtos = lista_produtos
        self.data_tempo = data_tempo