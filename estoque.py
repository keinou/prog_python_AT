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
    print(f"Produto '{descricao}' cadastrado com sucesso!")

def listar_produtos(ordem='asc'):
    """
    Lista todos os produtos
    """
    if ordem == 'asc':
        produtos_ordenados = sorted(estoque, key=lambda x: x['quantidade'])
    elif ordem == 'desc':
        produtos_ordenados = sorted(estoque, key=lambda x: x['quantidade'], reverse=True)
    else:
        produtos_ordenados = estoque

    for produto in produtos_ordenados:
        print(f"Descricao: {produto['descricao']}, Codigo: {produto['codigo']}, "
              f"Quantidade: {produto['quantidade']}, Custo: {produto['custo']:.2f}, "
              f"Preço de Venda: {produto['preco_venda']:.2f}")

def buscar_produto(*, descricao=None, codigo=None):
    """
    Busca produtos no estoque
    """
    resultados = []
    if descricao:
        resultados = [p for p in estoque if descricao.lower() in p['descricao'].lower()]
    elif codigo:
        resultados = [p for p in estoque if p['codigo'] == codigo]

    if not resultados:
        print("Produto nao encontrado")
    else:
        for produto in resultados:
            print(f"Descricao: {produto['descricao']}, Codigo: {produto['codigo']}, "
                  f"Quantidade: {produto['quantidade']}, Custo: {produto['custo']:.2f}, "
                  f"Preco de Venda: {produto['preco_venda']:.2f}")

def remover_produto(codigo):
    """
    Remove um produto do estoque com base no codigo fornecido
    """
    global estoque
    estoque = [p for p in estoque if p['codigo'] != codigo]
    print(f"Produto de código {codigo} removido com sucesso!")

def atualizar_estoque(codigo, nova_quantidade):
    """
    Atualiza a quantidade de um produto
    """
    for produto in estoque:
        if produto['codigo'] == codigo:
            produto['quantidade'] = nova_quantidade
            print(f"Quantidade do produto '{produto['descricao']}' atualizada para {nova_quantidade}")
            return
    print(f"Produto de código {codigo} anao encontrado")

def atualizar_preco(codigo, novo_preco):
    """
    Atualiza o preco de venda
    """
    for produto in estoque:
        if produto['codigo'] == codigo:
            if novo_preco < produto['custo']:
                print("Erro: O preço de venda nao pode ser inferior ao custo do item")
                return
            produto['preco_venda'] = novo_preco
            print(f"Preco de venda do produto '{produto['descricao']}' atualizado para {novo_preco:.2f}")
            return
    print(f"Produto de codigo {codigo} nao encontrado")
