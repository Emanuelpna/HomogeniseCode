from utils import send_GET_request, send_POST_request, encontra_item_na_lista

def test_modifyuser_nome_usuarios(client, captured_templates):
    maria_user = {
        'email': 'maria@email.com',
        'firstName': 'maria', 
        'password1': '1234567', 
        'password2': '1234567'
    }

    send_POST_request('/sign-up', maria_user, client, captured_templates)
        
    data = send_GET_request('/modifyuser', client, captured_templates)
    
    output_data = data.get('output_data')
    
    assert type(output_data) == list

    lista_nome = encontra_item_na_lista(output_data, 1, 'maria')

    assert len(lista_nome) > 0

def test_modifyuser_listagem_usuarios(client, captured_templates):
    data = send_GET_request('/modifyuser', client, captured_templates)
    output_data = data.get('output_data')
    assert type(output_data) == list

def test_modifyuser_listagem_usuarios_post(client, captured_templates):
    data = send_POST_request('/modifyuser', {'username_search': ''}, client, captured_templates)
    output_data = data.get('output_data')
    assert type(output_data) == list

