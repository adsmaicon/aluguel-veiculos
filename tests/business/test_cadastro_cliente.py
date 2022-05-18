from unittest import TestCase
from src.entities.cliente import Cliente
from src.business.cadastro_cliente import CadastroCliente


class TestCadastroCliente(TestCase):

    def test_inserir_cliente(self):
        # dado
        cliente = Cliente('1', 'rua 1', '9988-4433', 'Maicon')
        cadastro = CadastroCliente()
        
        # quanto
        cadastro.inserir(cliente)
        resultado = cadastro.listar_todos()

        # entao
        self.assertTrue(resultado[-1].nome == 'Maicon')


    def test_retorno_inserir_cliente(self):
        # dado
        cliente = Cliente('1', 'rua 1', '9988-4433', 'Maicon')
        cadastro = CadastroCliente()
        
        # quanto
        resultado = cadastro.inserir(cliente)

        # entao
        self.assertTrue(resultado == None)
        
