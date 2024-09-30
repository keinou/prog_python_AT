"""
Modulo para geracao de relatorio
"""

from estoque import estoque

def valor_total_estoque():
    """
    Calcula o valor total do estoque
    """
    valor_total = sum(p['quantidade'] * p['preco_venda'] for p in estoque)
    print(f"Valor total do estoque: R$ {valor_total:.2f}")

def calcular_lucro_presumido():
    """
    Calcula o lucro presumido
    """
    lucro_total = sum((p['preco_venda'] - p['custo']) * p['quantidade'] for p in estoque)
    print(f"Lucro presumido do estoque: R$ {lucro_total:.2f} ")

def gerar_relatorio_geral():
    """
    Gera um relatorio geral do estoque
    """
    print("\n--- Relatorio Geral do Estoque ---")
    print(f"{'Descricao'.ljust(25)}{'Codigo'.rjust(10)}{'Quantidade'.rjust(15)}"
          f"{'Custo'.rjust(15)}{'Preco Venda'.rjust(15)}{'Valor Total'.rjust(15)}")
    custo_total = 0
    faturamento_total = 0

    for produto in estoque:
        valor_total = produto['quantidade'] * produto['preco_venda']
        custo_total += produto['custo'] * produto['quantidade']
        faturamento_total += valor_total
        print(f"{produto['descricao'].ljust(25)}{str(produto['codigo']).rjust(10)}"
              f"{str(produto['quantidade']).rjust(15)}{str(produto['custo']).rjust(15)}"
              f"{str(produto['preco_venda']).rjust(15)}{str(valor_total).rjust(15)}")

    print("\nCusto total do estoque: R$ {:.2f}".format(custo_total))
    print("Faturamento total do estoque: R$ {:.2f}".format(faturamento_total))
