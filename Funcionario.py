from Venda import Venda

class Funcionario:
    def __init__(self, numero_clt, data_admissao):
        super()
        self.numero_clt = numero_clt
        self.data_admissao = data_admissao
        self.lista_transacoes:list[Venda] = []