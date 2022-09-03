# Gerenciamento de Mercearia

## Features:

 - Cadastro / Alteração / Remoção de:
    - Categorias
    - Produtos
    - Fornecedor
    - Cliente
    - Funcionário
 - Caixa
 - Relatórios de:
    - Vendas (geral)
    - Vendas (por data)
    - Vendas (produtos mais vendidos)
    - Vendas (clientes que mais compram)

## Requisitos:

 - O armazenamento será em arquivo

## Modelos:

- Produto
   - Id
   - Nome
   - IdCategoria
   - PrecoCompra
   - PrecoVenda

- Categoria
   - Id Categoria
   - Nome Categoria

- Pessoa (abstrata)
   - Nome Completo
   - Nome Resumido
   - CPF
   - RG

- Cliente(Pessoa)
   - IdCliente
   - ListaTransacoes (Compra/Venda)

- Funcionario(Pessoa)
   - IdFuncionario
   - NumeroClt
   - DataAdmissao
   - DataRescisao
   - ListaTransacoes (Compra/Venda)

- Venda
   - IdVenda
   - IdCliente (nullable)
   - IdFuncionario (obrigatório)
   - IdCaixa
   - ListaProdutos
   - DataTempo

- Fornecedor
   - IdFornecedor
   - NomeFornecedor
   - ListaProdutosFornecidos

- Caixa
   - Id
   - IdFuncionarioAtual
   - ListaTransacoes (Compra/Venda)
   - ListaAberturasFechamentos (DataTempo)

 - AberturaFechamentoBase (abstrata)
   - Id
   - IdCaixa
   - AberturaFechamentoEnum (1 - Abertura | 2 - Fechamento)
   - DataTempoAberturaFechamento

- Abertura(AberturaFechamentoBase)

- Fechamento(AberturaFechamentoBAse)

- Relatorio
   - Tipo
      - Vendas (geral)
      - Vendas (por data) 
      - Vendas (produtos mais vendidos) 
      - Vendas (clientes que mais compram)