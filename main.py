import os



def menu(titulo, opcoes):
    while True:
        print("=" * len(titulo), titulo, "=" * len(titulo), sep="\n")
        for i, (opcao, funcao) in enumerate(opcoes, 1):
            print("[{}] - {}".format(i, opcao))
        print("[{}] - Retornar/Sair".format(i+1))
        op = input("Opção: ")
        if op.isdigit():            
            if int(op) == i + 1:
                # Encerra este menu e retorna a função anterior
                break
            if int(op) <= len(opcoes):
                # Chama a função do menu:
                opcoes[int(op) - 1][1]()
                continue
        print("Opção inválida. \n\n")


def principal():
    opcoes = [
        ("Cadastro de clientes", clientes),
        ("Cadastro de veículos", veiculos),
        ("Alugueis", alugueis),
        ("Devoluções", develucoes),
    ]
    return menu("# MENU PRICIPAL #", opcoes)


def clientes():
    opcoes = [
        ("Inserir pessoa física", selecionar_opcoes),
        ("Inserir pessoa juridica", selecionar_opcoes),
        ("Consultar cliente", selecionar_opcoes),
        ("Remover cliente", selecionar_opcoes),
        ("Listar todos", selecionar_opcoes),
    ]
    return menu("# MENU DE CLIENTES #", opcoes)


def veiculos():
    opcoes = [
        ("Inserir automóvel", selecionar_opcoes),
        ("Inserir caminhão", selecionar_opcoes),
        ("Consultar veículo", selecionar_opcoes),
        ("Remover veículo", selecionar_opcoes),
        ("Listar todos", selecionar_opcoes),
    ]
    return menu("# MENU DE VEÍCULOS #", opcoes)


def alugueis():
    opcoes = [
        ("Registar aluguel", selecionar_opcoes),
        ("Consultar aluguel", selecionar_opcoes),
        ("Listar alugueis ativos", selecionar_opcoes),
        ("Listar todos os alugueis", selecionar_opcoes),
    ]
    return menu("# MENU DE ALUGUÉIS #", opcoes)



def develucoes():
    opcoes = [
        ("Registrar devolução", selecionar_opcoes),
        ("Listar alugueis concluídos", selecionar_opcoes),
        ("Listar todos os alugueis", selecionar_opcoes),
    ]
    return menu("# MENU DE DEVOLUÇÕES #", opcoes)


def selecionar_opcoes():
    print("teste")


if __name__ == "__main__":
    principal()
