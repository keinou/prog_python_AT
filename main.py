"""
Modulo principal que executa o sistema
"""

from estoque import carregar_estoque_inicial, cadastrar_produto

def menu():
    print("\n--- Sistema de Controle de Estoque | by Karc.io ---")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Buscar produto")
    print("4. Remover produto")
    print("5. Atualizar estoque")
    print("6. Atualizar preço")
    print("7. Gerar relatorio geral")
    print("8. Sair")
    return input("Escolha uma opcao: ")

def main():
    estoque_inicial = "Notebook Dell;201;15;3200.00;4500.00#Notebook Lenovo;202;10;2800.00;4200.00"
    carregar_estoque_inicial(estoque_inicial)

    while True:
        opcao = menu()
        if opcao == '1':
            descricao = input("Descricao do produto: ")
            codigo = int(input("Codigo do produto: "))
            quantidade = int(input("Quantidade: "))
            custo = float(input("Custo do item: "))
            preco_venda = float(input("Preco de venda: "))
            cadastrar_produto(descricao, codigo, quantidade, custo, preco_venda)
        elif opcao == '8':
            print("Saindo do sistema...")
            break
        else:
            print("Opcao invalida! Tente novamente")

if __name__ == "__main__":
    main()
