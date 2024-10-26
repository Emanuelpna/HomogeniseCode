from utils import send_GET_request, send_POST_request

def test_usertype_listagem_usuarios(client, captured_templates):
    data = send_GET_request('/usertype', client, captured_templates)
    output_data = data.get('output_data')
    assert type(output_data) == list

def test_usertype_administrador_usuarios(client, captured_templates):
    send_POST_request('/usertypedata', {'user_type_name': 'administrador'}, client, captured_templates, {'type_operation' : 'A'})
    data = send_POST_request('/usertype', {'usertype_search': 'administrador'}, client, captured_templates)
    output_data = data.get('output_data')
    assert type(output_data) == list
    lista_adm = list(filter(lambda x: x[1] == 'administrador', output_data))
    assert len(lista_adm) > 0

def test_usertype_listagem_usuarios_filtro_vazio(client, captured_templates):
    data = send_POST_request('/usertype', {'usertype_search': ''}, client, captured_templates)
    output_data = data.get('output_data')
    assert type(output_data) == list
