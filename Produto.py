from Categoria import Categoria


class Produto:
    def __init__(self, nome, categoria: Categoria, preco_compra, preco_venda):
        self.nome = nome
        self.preco_compra = preco_compra
        self.categoria = categoria
        self.preco_venda = preco_venda