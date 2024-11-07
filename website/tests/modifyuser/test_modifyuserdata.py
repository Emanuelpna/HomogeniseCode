from uuid import uuid4

from utils import send_GET_request, send_POST_request

def test_modificar_usuario_com_senhas_diferentes(client, captured_templates):
    """
        [TC013 - ?] Não modificar usuário com senhas 1 e 2 não idênticas

    """

    sign_up_data = {
        'email': 'test'+ uuid4().hex + '@example.com',
        'firstName': 'NewUser',
        'password1': 'password123',
        'password2': 'password123'
    }

    send_POST_request('/sign-up', sign_up_data, client, captured_templates)

    modify_data = {
        'user_id': '1',
        'user_type_id': '1',
        'first_name':'User',
        'password1':'newpassword123',
        'password2':'newpassword',
    }

    send_POST_request('/modifyuserdata', modify_data, client, captured_templates)

    data =  send_GET_request('/modifyuser', client, captured_templates)

    output_data = data.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[2] == sign_up_data.get('email'), output_data))

    assert updated_entry[0][1] == sign_up_data.get('firstName')


def test_modificar_usuario_com_senhas_com_poucos_caracteres(client, captured_templates):
    """
        [TC0013 - ?] Não modificar usuário com senha com poucos caracteres
    """

    sign_up_data = {
        'email': 'test'+ uuid4().hex + '@example.com',
        'firstName': 'NewUser',
        'password1': 'newpassword123',
        'password2': 'newpassword123'
    }

    send_POST_request('/sign-up', sign_up_data, client, captured_templates)

    modify_data = {
        'user_id': '1',
        'user_type_id': '1',
        'first_name':'User',
        'password1':'1',
        'password2':'1',
    }

    send_POST_request('/modifyuserdata', modify_data, client, captured_templates)

    data =  send_GET_request('/modifyuser', client, captured_templates)

    output_data = data.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[2] == sign_up_data.get('email'), output_data))

    assert updated_entry[0][1] == sign_up_data.get('firstName')