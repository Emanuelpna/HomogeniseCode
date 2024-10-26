from utils import send_GET_request, send_POST_request

def test_app_is_created(app):
    assert app.name == 'website'

def test_request_returns_404(client):
    assert client.get('/url_que_não_existe').status_code == 404
    
def test_request_researchline(client, captured_templates):
    data = send_GET_request('/researchline', client, captured_templates)

    assert len(data.get('output_data')) > 0

