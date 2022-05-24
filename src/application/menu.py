

class Menu():

    @staticmethod
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

    @staticmethod
    def principal():
        opcoes = [
            ("Cadastro de clientes", Menu.clientes),
            ("Cadastro de veículos", Menu.veiculos),
            ("Alugueis", Menu.alugueis),
            ("Devoluções", Menu.develucoes),
        ]
        return Menu.menu("# MENU PRICIPAL #", opcoes)

    @staticmethod
    def clientes():
        opcoes = [
            ("Inserir pessoa física", Menu.selecionar_opcoes),
            ("Inserir pessoa juridica", Menu.selecionar_opcoes),
            ("Consultar cliente", Menu.selecionar_opcoes),
            ("Remover cliente", Menu.selecionar_opcoes),
            ("Listar todos", Menu.selecionar_opcoes),
        ]
        return Menu.menu("# MENU DE CLIENTES #", opcoes)

    @staticmethod
    def veiculos():
        opcoes = [
            ("Inserir automóvel", Menu.selecionar_opcoes),
            ("Inserir caminhão", Menu.selecionar_opcoes),
            ("Consultar veículo", Menu.selecionar_opcoes),
            ("Remover veículo", Menu.selecionar_opcoes),
            ("Listar todos", Menu.selecionar_opcoes),
        ]
        return Menu.menu("# MENU DE VEÍCULOS #", opcoes)

    @staticmethod
    def alugueis():
        opcoes = [
            ("Registar aluguel", Menu.selecionar_opcoes),
            ("Consultar aluguel", Menu.selecionar_opcoes),
            ("Listar alugueis ativos", Menu.selecionar_opcoes),
            ("Listar todos os alugueis", Menu.selecionar_opcoes),
        ]
        return Menu.menu("# MENU DE ALUGUÉIS #", opcoes)

    @staticmethod
    def develucoes():
        opcoes = [
            ("Registrar devolução", Menu.selecionar_opcoes),
            ("Listar alugueis concluídos", Menu.selecionar_opcoes),
            ("Listar todos os alugueis", Menu.selecionar_opcoes),
        ]
        return Menu.menu("# MENU DE DEVOLUÇÕES #", opcoes)

    @staticmethod
    def selecionar_opcoes():
        print("teste")
