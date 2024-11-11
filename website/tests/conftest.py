from flask import template_rendered
import pytest

from website import create_app

@pytest.fixture(scope="session")
def app():
    """Instância do App Flask similar ao que é acessado no navegador"""
    return create_app()

@pytest.fixture(scope="function", autouse=True)
def loginUser(client):
    client.post('/sign-up', data={'email': 'teste@email.com', 'firstName': 'Teste', 'password1': '1234567', 'password2': '1234567'})
    client.post('/login', data={'email': 'teste@email.com', 'password': '1234567'})

@pytest.fixture
def captured_templates(app):
    # Lista de valores capturados do template
    recorded = []

    # Função que é chamada ao renderizar um template
    def record(sender, template, context, **extra):
        # Salva no array `record` as informações que foram usadas no template
        recorded.append((template, context))

    # Conecta nossa função no renderizador de templates do Flask
    template_rendered.connect(record, app)

    try:
        # Envia para os testes cada um dos resultados recebidos acima
        yield recorded
    finally:
        template_rendered.disconnect(record, app)