"""
Modulo para gerenciamento de estoque
"""

estoque = []

def carregar_estoque_inicial(estoque_inicial):
    """
    Processa o estoque inicial
    """
    produtos = estoque_inicial.split("#")
    for produto in produtos:
        descricao, codigo, quantidade, custo, preco_venda = produto.split(";")
        estoque.append({
            'descricao': descricao,
            'codigo': int(codigo),
            'quantidade': int(quantidade),
            'custo': float(custo),
            'preco_venda': float(preco_venda)
        })

def cadastrar_produto(descricao, codigo, quantidade, custo, preco_venda):
    """
    Cadastra um novo produto no estoque.
    """
    # Verifica se o codigo do prod ja existe
    for item in estoque:
        if item['codigo'] == codigo:
            print(f"Erro: Código {codigo} ja existe no estoque")
            return
    estoque.append({
        'descricao': descricao,
        'codigo': codigo,
        'quantidade': quantidade,
        'custo': custo,
        'preco_venda': preco_venda
    })
    print(f"Produto {descricao} cadastrado com sucesso!")

# Exemplo
estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00"
carregar_estoque_inicial(estoque_inicial)
