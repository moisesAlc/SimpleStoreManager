

from DAOs import DAOs
from . import Categoria, Estoque, Produto, Fornecedor, Pessoa, Funcionario, Venda
from DAOs import DaoEstoque, DAOFornecedor, DAOPessoa, DaoFuncionario
from datetime import datetime, date

class ControllerCategoria:

    def cadastrarCategoria(selfself, novaCategoria):
        existe = False

