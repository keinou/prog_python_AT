"""
Modulo principal que executa o sistema
"""

from estoque import carregar_estoque_inicial, cadastrar_produto, listar_produtos, buscar_produto, remover_produto, atualizar_estoque, atualizar_preco
from relatorios import valor_total_estoque, calcular_lucro_presumido, gerar_relatorio_geral

def menu():
    print("\n--- Sistema de Controle de Estoque | by Karc.io ---")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Buscar produto")
    print("4. Remover produto")
    print("5. Atualizar estoque")
    print("6. Atualizar preço")
    print("7. Gerar relatorio geral")
    print("8. Valor total do estoque")
    print("9. Calcular lucro presumido")
    print("10. Sair")
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
        elif opcao == '2':
            ordem = input("Ordenar por quantidade (asc/desc): ").strip()
            listar_produtos(ordem)
        elif opcao == '3':
            busca_descricao = input("Buscar por descricao (vazio para buscar por codigo): ").strip()
            if busca_descricao:
                buscar_produto(descricao=busca_descricao)
            else:
                codigo = int(input("Buscar por codigo: "))
                buscar_produto(codigo=codigo)
        elif opcao == '4':
            codigo = int(input("Codigo do produto a ser removido: "))
            remover_produto(codigo)
        elif opcao == '5':
            codigo = int(input("Codigo do produto para atualizar quantidade: "))
            nova_quantidade = int(input("Nova quantidade: "))
            atualizar_estoque(codigo, nova_quantidade)
        elif opcao == '6':
            codigo = int(input("Codigo do produto para atualizar preço: "))
            novo_preco = float(input("Novo preco de venda: "))
            atualizar_preco(codigo, novo_preco)
        elif opcao == '7':
            gerar_relatorio_geral()
        elif opcao == '8':
            valor_total_estoque()
        elif opcao == '9':
            calcular_lucro_presumido()
        elif opcao == '10':
            print("Saindo do sistema...")
            break
        else:
            print("Opcao invalida! Tente novamente")

if __name__ == "__main__":
    main()