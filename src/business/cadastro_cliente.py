import mysql.connector
from src.entities.cliente import Cliente
from src.entities.pessoa_fisica import PessoaFisica
from src.entities.pessoal_juridica import PessoaJuridica
from src.exceptions.cliente_not_found_error import ClienteNotFoundError
from src.exceptions.not_found_error import NotFoundError
from .cadastro_abstract import CadastroAbtract


class CadastroCliente(CadastroAbtract):

    def inserir(self, cliente: Cliente) -> None:
        cnx = mysql.connector.connect(user='maicon', password='123456',
                                      host='127.0.0.1',
                                      database='mydb')
        cursor = cnx.cursor()
        adiciona_cliente = ("INSERT INTO cliente "
                            "(nome, endereco, telefone, cpf, cnpj, tipo)"
                            " VALUES ( %(nome)s, %(endereco)s, %(telefone)s, %(cpf)s, %(cnpj)s, %(tipo)s)")

        cursor.execute(adiciona_cliente, {
            "nome": cliente.nome,
            "endereco": cliente.endereco,
            "telefone": cliente.telefone,
            "cpf": cliente.cpf if cliente.cpf else '',
            "cnpj": cliente.cnpj if cliente.cnpj else '',
            "tipo": 'fisica' if cliente.cpf else 'juridica'
        })
        cnx.commit()

        cursor.close()
        cnx.close()

    def consultar(self, id: str) -> Cliente:
        cnx = mysql.connector.connect(user='maicon', password='123456',
                                      host='127.0.0.1',
                                      database='mydb')
        cursor = cnx.cursor()

        query = ("SELECT id, nome, endereco, telefone, cpf, cnpj, tipo FROM cliente WHERE id=%s")

        cursor.execute(query, [id])

        for (id, nome, endereco, telefone, cpf, cnpj, tipo) in cursor:
            if tipo == 'fisica':
                cliente = PessoaFisica(id, endereco, telefone, cpf, nome)
            else:
                cliente = PessoaJuridica(id, endereco, telefone, cnpj, nome)
        else:
            raise ClienteNotFoundError("Cliente não encontrado.")

        cursor.close()
        cnx.close()

        return cliente
