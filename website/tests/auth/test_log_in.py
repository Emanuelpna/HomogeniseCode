from uuid import uuid4

from utils import send_GET_request, send_POST_request

def test_log_in_usuario_existente_senha_correta(client, captured_templates):
    """
        [TC008 - ?] Tentar realizar o Login com usuário existente, senha correta

    """

    sign_up_data = {
        'email': 'test'+ uuid4().hex + '@example.com',
        'firstName': 'NewUser',
        'password1': 'newpassword123',
        'password2': 'newpassword123'
    }

    send_POST_request('/sign-up', sign_up_data, client, captured_templates)

    login_data = {
        'email': 'test'+ uuid4().hex + '@example.com',
        'password': 'newpassword123'
    }

    send_POST_request('/login', login_data, client, captured_templates)

    data =  send_GET_request('/modifyuser', client, captured_templates)

    output_data = data.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[2] == sign_up_data.get('password'), output_data))

    assert len(updated_entry) == 0

def test_log_in_usuario_existente_senha_incorreta(client, captured_templates):
    """
        [TC008 - ?] não realizar o Login com usuário existente, senha incorreta

    """

    sign_up_data = {
        'email': 'test'+ uuid4().hex + '@example.com',
        'firstName': 'NewUser',
        'password1': 'newpassword123',
        'password2': 'newpassword123'
    }

    send_POST_request('/sign-up', sign_up_data, client, captured_templates)

    login_data = {
        'email': 'test'+ uuid4().hex + '@example.com',
        'password': 'wrongpassword'
    }

    send_POST_request('/login', login_data, client, captured_templates)

    data =  send_GET_request('/modifyuser', client, captured_templates)

    output_data = data.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[2] == sign_up_data.get('password'), output_data))

    assert len(updated_entry) == 0

def test_log_in_usuario_inexistente(client, captured_templates):
    """
        [TC008 - ?] login com usuario inexistente
    """

    sign_up_data = {
        'email': 'test'+ uuid4().hex + '@example.com',
        'firstName': 'NewUser',
        'password1': 'newpassword123',
        'password2': 'newpassword123'
    }

    send_POST_request('/sign-up', sign_up_data, client, captured_templates)

    login_data = {
        'email': 'test',
        'password': 'newpassword123'
    }

    send_POST_request('/login', login_data, client, captured_templates)

    data =  send_GET_request('/modifyuser', client, captured_templates)

    output_data = data.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[2] == sign_up_data.get('email'), output_data))

    assert len(updated_entry) == 1

