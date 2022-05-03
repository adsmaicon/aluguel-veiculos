from src.business.cadastro_cliente import CadastroCliente
from src.entities.cliente import Cliente
from src.entities.pessoa_fisica import PessoaFisica
from src.entities.pessoal_juridica import PessoaJuridica


cliente = Cliente('1', 'rua 1', '9988-4433', 'Maicon')
cliente_pessoa_fisica = PessoaFisica(
    '2', 'rua 2', '9999-5555', '542.521.532-85', 'Henrique')
cliente_pessoa_juridica = PessoaJuridica(
    '3', 'rua 3', '9999-7777', '12.169.185/0001-42', 'Henrique LTDA')

cadastro = CadastroCliente()

cadastro.inserir(cliente)

cadastro.inserir(cliente_pessoa_fisica)

cadastro.inserir(cliente_pessoa_juridica)

cadastro.consultar('1')