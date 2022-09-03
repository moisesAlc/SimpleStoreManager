# -*- coding: UTF-8 -*-

from Produto import Produto
from Categoria import Categoria
from Venda import Venda


class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = []
        for i in cls.categoria:
            cat.append(Categoria(i))

        return cat


class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(f"VENDA: ---------------------------------\n")
            arq.writelines(
                f"Id Cliente: {venda.id_cliente if venda.id_cliente else '-'}\n")
            arq.writelines(
                f"Id Funcionario: {venda.id_funcionario if venda.id_funcionario else '-'}\n")
            arq.writelines(
                f"Id Caixa: {venda.id_caixa if venda.id_caixa else '-'}\n")
            for produto in venda.lista_produtos:
                arq.writelines(f"   Nome Produto: {produto.nome}\n")
                arq.writelines(f"   Categoria: {produto.categoria.nome}\n")
                arq.writelines(f"   Preço Compra: {produto.preco_compra}\n")
                arq.writelines(
                    f"   Lucro Venda: {produto.preco_compra - produto.preco_venda}\n")
            arq.writelines(f"Data/Hora da Venda: {venda.data_tempo}\n")
            arq.writelines('------------------------------------------\n\n')

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()

        #cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        print(cls.venda)


categoria = Categoria('fruta')

produto = Produto('banana', categoria, 5.65, 3.95)

venda = Venda(None, None, None, [produto])

DaoVenda.salvar(venda)
DaoVenda.ler()

# DaoCategoria.salvar('frutas')
# DaoCategoria.salvar('verduras')
# DaoCategoria.salvar('legumes')

# DaoCategoria.ler()
