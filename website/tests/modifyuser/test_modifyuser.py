from utils import send_GET_request, send_POST_request

# def test_modifyuser_nome_usuarios(client, captured_templates):
#     data = send_POST_request('/modifyuser', {'first_name': 'maria'}, client, captured_templates)
#     output_data = data.get('output_data')
#     assert type(output_data) == list
#     lista_nome = list(filter(lambda x: x[1] == 'maria', output_data))
#     assert len(lista_nome) > 0

def test_modifyuser_listagem_usuarios(client, captured_templates):
    data = send_GET_request('/modifyuser', client, captured_templates)
    output_data = data.get('output_data')
    assert type(output_data) == list

def test_modifyuser_listagem_usuarios_post(client, captured_templates):
    data = send_POST_request('/modifyuser', {'username_search': ''}, client, captured_templates)
    output_data = data.get('output_data')
    assert type(output_data) == list

