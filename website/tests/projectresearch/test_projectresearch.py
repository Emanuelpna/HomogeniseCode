from utils import send_GET_request, send_POST_request
from uuid import uuid4

def test_projectresearch_pegar_todos_os_projetos(client, captured_templates):
    data = send_GET_request('/projectresearch', client, captured_templates)
    output_data = data.get('output_data')
    assert len(output_data) > 0

def test_projectresearch_post_sem_pesquisa(client, captured_templates):
    # Teste POST com campo de pesquisa vazio
    response = client.post('/projectresearch', data={'project_search': ''})
    assert response.status_code == 200
    assert b'' in response.data

def test_projectresearch_post_com_pesquisa(client, captured_templates):
    # Teste POST com campo de pesquisa preenchido
    response = client.post('/projectresearch', data={'project_search': 'Project'})
    assert response.status_code == 200
    assert b'Project' in response.data