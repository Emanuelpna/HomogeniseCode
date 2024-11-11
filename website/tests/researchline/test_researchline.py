from utils import send_GET_request, send_POST_request
from uuid import uuid4

def test_request_researchline(client, captured_templates):
    data = send_GET_request('/researchline', client, captured_templates)

    output_data = data.get('output_data')

    assert len(output_data) > 0

# def test_researchline_post_sem_pesquisa(client, captured_templates):
#     response = client.post('/researchline', data={'researchline': ''})
#     assert response.status_code == 500
#     assert b'' in response.data

# def test_researchline_post_com_pesquisa(client, captured_templates):
#     response = client.post('/researchline', data={'researchline': 'Projeto'})
#     assert response.status_code == 200
#     assert b'Projeto' in response.data