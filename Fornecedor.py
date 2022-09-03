from Produto import Produto

class Fornecedor:
    def __init__(self, nome_fornecedor):
        self.nome_fornecedor = nome_fornecedor
        self.lista_produtos_fornecidos:list[Produto] = []