# ex3.y :: refatorar a solução do exercício anterior de forma que ele fique mais organizado usando funções.
import os
import time

def obter_opcao() -> int:
    os.system("cls")
    print("Cadastro de Produtos")
    print("-" * 20)
    print("1) Cadastrar Produto")
    print("2) Listar Produtos")
    print("3) Sair")
    return int(input("Opção desejada: "))

def cadastrar_produto(produtos: dict, codigo: int):
    nome, descricao, categoria, preco, estoque, perecivel = ler_dados_produto()
    persistir_dados_produto(produtos, codigo, nome, descricao, categoria, preco, estoque, perecivel)

def ler_dados_produto():
    os.system("cls")
    print("Cadastrar Produto")
    print("-" * 17)
    nome = ler_dado("Nome", str, validar_nome_produto)
    descricao = ler_dado("Descrição", str, validar_descricao_produto)
    categoria = ler_dado("Categoria", str, validar_categoria_produto)
    preco = ler_dado("Preço", float, validar_preco_produto)
    estoque = ler_dado("Estoque", int, validar_estoque_produto)
    perecivel = ler_dado("Perecível (0=Não, 1=Sim)", bool, validar_perecivel_produto)
    return nome, descricao, categoria, preco, estoque, perecivel

def validar_nome_produto(nome: str) -> bool:
    if len(nome) < 2:
        print("O nome do produto deve ter 2 ou mais caracteres. Tente novamente.")
        return False
    else:
        return True
    
def validar_descricao_produto(descricao: str) -> bool:
    if len(descricao) < 12:
        print("O descrição do produto deve ter 12 ou mais caracteres. Tente novamente.")
        return False
    else:
        return True

def validar_categoria_produto(categoria: str) -> bool:
    if len(categoria) < 4:
        print("A categoria do produto deve ter 4 ou mais caracteres. Tente novamente.")
        return False
    else:
        return True
    
def validar_preco_produto(preco: float) -> bool:
    if preco <= 0:
        print("O preço do produto deve ser maior que zero. Tente novamente.")
        return False
    else:
        return True
    
def validar_estoque_produto(estoque: int) -> bool:
    if estoque < 0:
        print("O estoque do produto deve ser maior ou igual a zero. Tente novamente.")
        return False
    else:
        return True

def validar_perecivel_produto(perecivel: bool) -> bool:
    return True

def tentar_converter(valor, tipo):
    try:
        valor_convertido = tipo(valor)
    except ValueError:
        return False
    return valor_convertido

def ler_dado(titulo, tipo, validar_atributo):
    while True:
        atributo = input(f"{titulo}: ")
        atributo = tentar_converter(atributo, tipo)
        if not atributo:
            print(f"{titulo} deve ser um valor válido. Tente novamente.")
            continue
        if not validar_atributo(atributo):
            continue
        return atributo    

def persistir_dados_produto(produtos, codigo, nome, descricao, categoria, preco, estoque, perecivel):
    produtos[codigo] = (nome, descricao, categoria, preco, estoque, perecivel)
    print("Produto cadastrado com sucesso!")
    time.sleep(2)

def listar_produtos(produtos: dict):
    os.system("cls")
    print("Listar Produtos")
    print("-" * 47)
    print(f"Código {'Produto':15} {'Preço':>10} {'Estoque':>10}")
    print("-" * 47)
    for codigo, (nome, preco, estoque) in produtos.items():
        print(f"{codigo:06d} {nome:15} {preco:>10.2f} {estoque:>10d}")
    print("-" * 47)
    print("Pressione ENTER para voltar ao menu...", end="")
    input()
    print("Voltando ao menu...")
    time.sleep(2)

def sair():
    print("Saindo do sistema...")
    time.sleep(2)
    os.system("cls")

def main():
    produtos = {}
    codigo_produto = 1
    while True:
        opcao = obter_opcao()
        match opcao:
            case 1:
                cadastrar_produto(produtos, codigo_produto)
                codigo_produto = codigo_produto + 1
            case 2:
                listar_produtos(produtos)
            case 3:
                sair()
                break
            case _:
                print("Opção inválida. Voltando ao menu...")
                time.sleep(2)

if __name__ == "__main__": # dunder (double underline)
    main()