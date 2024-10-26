from uuid import uuid4

from utils import send_GET_request, send_POST_request

def test_registra_usuário_repetido_no_banco_de_dados(client, captured_templates):
    """
        [TC009 - A] Não criar usuário com e-mail repetido na base de dados

    """

    sign_up_data = {
        'email': 'test'+ uuid4().hex + '@example.com',
        'firstName': 'NewUser',
        'password1': 'newpassword123',
        'password2': 'newpassword123'
    }

    send_POST_request('/sign-up', sign_up_data, client, captured_templates)
    send_POST_request('/sign-up', sign_up_data, client, captured_templates)
    
    data =  send_GET_request('/modifyuser', client, captured_templates)

    output_data = data.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[2] == sign_up_data.get('email'), output_data))

    assert len(updated_entry) == 1

def test_resgistrar_email_com_pocuos_caracteres(client, captured_templates):
    """
        [TC009 - B] Não criar usuário com e-mail com poucos caracteres
    """

    sign_up_data = {
        'email': 'tes',
        'firstName': 'NewUser',
        'password1': 'newpassword123',
        'password2': 'newpassword123'
    }

    send_POST_request('/sign-up', sign_up_data, client, captured_templates)

    data =  send_GET_request('/modifyuser', client, captured_templates)

    output_data = data.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[2] == sign_up_data.get('email'), output_data))

    assert len(updated_entry) == 0

def test_resgistrar_usuario_com_nome_com_pocuos_caracteres(client, captured_templates):
    """
        [TC009 - C] Não criar usuário com primeiro nome com poucos caracteres
    """

    sign_up_data = {
        'email': 'test'+ uuid4().hex + '@example.com',
        'firstName': 'N',
        'password1': 'newpassword123',
        'password2': 'newpassword123'
    }

    send_POST_request('/sign-up', sign_up_data, client, captured_templates)

    data =  send_GET_request('/modifyuser', client, captured_templates)

    output_data = data.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[1] == sign_up_data.get('firstName'), output_data))

    assert len(updated_entry) == 0

def test_resgistrar_usuario_com_senhas_diferentes(client, captured_templates):
    """
        [TC009 - D] Não criar usuário com senhas 1 e 2 não idênticas

    """

    sign_up_data = {
        'email': 'test'+ uuid4().hex + '@example.com',
        'firstName': 'NewUser',
        'password1': 'newpassword123',
        'password2': 'newpassword000'
    }

    send_POST_request('/sign-up', sign_up_data, client, captured_templates)

    data =  send_GET_request('/modifyuser', client, captured_templates)

    output_data = data.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[2] == sign_up_data.get('email'), output_data))

    assert len(updated_entry) == 0


def test_resgistrar_usuario_com_senhas_com_poucos_caracteres(client, captured_templates):
    """
        [TC009 - E] Não criar usuário com senha com poucos caracteres


    """

    sign_up_data = {
        'email': 'test'+ uuid4().hex + '@example.com',
        'firstName': 'NewUser',
        'password1': '1',
        'password2': '1'
    }

    send_POST_request('/sign-up', sign_up_data, client, captured_templates)

    data =  send_GET_request('/modifyuser', client, captured_templates)

    output_data = data.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[2] == sign_up_data.get('email'), output_data))

    assert len(updated_entry) == 0

def test_resgistrar_um_novo_usuário_no_banco_de_dados(client, captured_templates):
    """
        [TC009 - F] Criar usuário com todos os dados especificados

    """

    sign_up_data = {
        'email': 'test'+ uuid4().hex + '@example.com',
        'firstName': 'NewUser',
        'password1': 'newpassword123',
        'password2': 'newpassword123'
    }

    send_POST_request('/sign-up', sign_up_data, client, captured_templates)

    data =  send_GET_request('/modifyuser', client, captured_templates)

    output_data = data.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[2] == sign_up_data.get('email'), output_data))

    assert len(updated_entry) == 1

def test_resgistrar_um_novo_usuário_no_banco_de_dados_usando_requisição_GET(client, captured_templates):
    """
        [TC009 - G] Nenhum resultado deve ser apresentado para requisição GET

    """

    data = send_GET_request('/sign-up', client, captured_templates)

    user = data.get('user')

    assert user != None
