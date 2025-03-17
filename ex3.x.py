# ex3.x :: Faça um programa que solicite continuamente ao usuário a digitação do nome, preço e estoque de um produto, salvando os dados em 3 coleções separadas, sendo que o nome do produto não pode se repetir. O programa deve oferecer 3 opções:
# 1) Cadastrar Produto
# 2) Listar Produtos
# 3) Sair
import os
import time

produtos = {}

while True:
    os.system("cls")
    print("Cadastro de Produtos")
    print("-" * 20)
    print("1) Cadastrar Produto")
    print("2) Listar Produtos")
    print("3) Sair")
    opcao = int(input("Opção desejada: "))
    match opcao:
        case 1:
            os.system("cls")
            print("Cadastrar Produto")
            print("-" * 17)
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))
            produtos[nome] = (preco, estoque)
            print("Produto cadastrado com sucesso!")
            time.sleep(2)
        case 2:
            os.system("cls")
            print("Listar Produtos")
            print("-" * 40)
            print(f"{'Produto':15} {'Preço':>10} {'Estoque':>10}")
            print("-" * 40)
            for nome, (preco, estoque) in produtos.items():
                print(f"{nome:15} {preco:>10.2f} {estoque:>10d}")
            print("-" * 40)
            print("Pressione ENTER para voltar ao menu...", end="")
            input()
            print("Voltando ao menu...")
            time.sleep(2)
        case 3:
            print("Saindo do sistema...")
            time.sleep(2)
            os.system("cls")
        case _:
            print("Opção inválida. Voltando ao menu...")
            time.sleep(2)