import pytest
import app
from src.business.cadastro_cliente import CadastroCliente


@pytest.fixture()
def client():
    app.cadastro_cliente = CadastroCliente()
    return app.app.test_client()


def test_inserir_cliente(client):
    # Dado
    # Quando
    response = client.post("/cliente", json={
        "id": "1",
        "endereco": "Rua teste",
        "telefone": "41 9896-4561",
        "cpf": "123.123.123-75",
        "nome": "Teste de API"
    })

    # Entao
    assert response.status_code == 201


def test_busca_clientes_empty(client):
    # Dado
    # Quando
    response = client.get("/cliente")

    # Entao
    assert response.json == []


def test_busca_clientes(client):
    # Dado
    # Quando
    response = client.get("/cliente")

    # Entao
    assert response.status_code == 200


def test_busca_cliente_404(client):
    # Dado
    # Quando
    response = client.get("/cliente/123")

    # Entao
    assert response.status_code == 404


def test_consultar_cliente(client):
    # Dado
    client.post("/cliente", json={
        "id": "1",
        "endereco": "Rua teste",
        "telefone": "41 9896-4561",
        "cpf": "123.123.123-75",
        "nome": "Teste de API"
    })
    client.post("/cliente", json={
        "id": "2",
        "endereco": "Rua teste 2",
        "telefone": "41 9896-9844",
        "cpf": "987.987.987-54",
        "nome": "Teste de API 2"
    })

    # Quando
    response = client.get("/cliente/1")

    # Entao
    assert response.json == {
        "id": "1",
        "endereco": "Rua teste",
        "telefone": "41 9896-4561",
        "cpf": "123.123.123-75",
        "nome": "Teste de API"
    }


def test_remover_cliente(client):
    # Dado
    client.post("/cliente", json={
        "id": "1",
        "endereco": "Rua teste",
        "telefone": "41 9896-4561",
        "cpf": "123.123.123-75",
        "nome": "Teste de API"
    })
    client.post("/cliente", json={
        "id": "2",
        "endereco": "Rua teste 2",
        "telefone": "41 9896-9844",
        "cpf": "987.987.987-54",
        "nome": "Teste de API 2"
    })

    # Quando
    client.delete("/cliente/1")

    # Entao
    response = client.get("/cliente/1")
    assert response.status_code == 404
