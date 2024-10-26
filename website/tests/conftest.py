from flask import template_rendered
import pytest

from website import create_app

@pytest.fixture(scope="session")
def app():
    """Instância do App Flask similar ao que é acessado no navegador"""
    return create_app()

@pytest.fixture(scope="function", autouse=True)
def loginUser(client):
    client.post('/login', data={'email': 'teste@email.com', 'password': '1234567'})

@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)

    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)