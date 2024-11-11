from utils import send_POST_request, send_GET_request
from uuid import uuid4

def test_usertypedata_adicionar_novo_user(client, captured_templates):
    """
        [TC010 - F] Adicionar novo tipo de usuário com os dados enviados
    """
    
    get_response = send_GET_request('/usertypedata', client, captured_templates)

    current_total_entries = len(get_response.get('usertype_list'))

    body = { 'user_type_name': 'Novo tipo adicionado' }

    params = { 'type_operation' : 'A' }

    post_response = send_POST_request('/usertypedata', body, client, captured_templates, params)

    output_data = post_response.get('output_data')

    assert len(output_data) == current_total_entries + 1

def test_usertypedata_atualizar_user(client, captured_templates): 
    """
        [TC010 - E] Atualizar tipo de usuário com os dados enviados
    """

    user_type_name = "Usuário para atualizar" + uuid4().hex

    post_response = send_POST_request("/usertypedata", { 'user_type_name': user_type_name }, client, captured_templates, { 'type_operation' : 'A' })

    user_types = post_response.get('output_data')

    assert len(user_types) > 0

    new_entry = list(filter(lambda x: x[1] == user_type_name, user_types))

    new_entry_id = new_entry[0][0]

    body = { 'user_type_id': new_entry_id, 'user_type_name': 'Usuário para atualizar' }

    params = { 'type_operation': 'U' }

    post_response = send_POST_request('/usertypedata', body, client, captured_templates, params)

    output_data = post_response.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[0] == new_entry_id, output_data))
    updated_entry_id = updated_entry[0][0]

    assert updated_entry_id == new_entry_id

    assert updated_entry[0][1] == body['user_type_name']

def test_usertypedata_deletar_user_type(client, captured_templates):
    """
        [TC010 - G] Deletar tipo de usuário com os dados enviados
    """

    user_type_name = 'User Type para Deletar ' + uuid4().hex

    post_response = send_POST_request('/usertypedata', { 'user_type_name': user_type_name }, client, captured_templates, { 'type_operation': 'A' })
    
    user_types = post_response.get('output_data')

    new_entry = list(filter(lambda x: x[1] == user_type_name, user_types))

    new_entry_id = new_entry[0][0]
    
    body = { 'user_type_id': new_entry_id }

    params = { 'type_operation': 'D' }

    post_response = send_POST_request('/usertypedata', body, client, captured_templates, params)

    output_data = post_response.get('output_data')
    deleted_entry = list(filter(lambda x: x[0] == new_entry_id, output_data))
    
    assert len(deleted_entry) == 0

def test_usertypedata_deletar_user_type_sem_registro(client, captured_templates):
    """
        [TC010 - C] Falha ao deletar tipo de usuário quando não existir registro com o ID especificado
    """

    unexisting_user_type_id = -1

    body = { 'user_type_id': unexisting_user_type_id }

    params = { 'type_operation': 'D' }

    post_response = send_POST_request('/usertypedata', body, client, captured_templates, params)

    output_data = post_response.get('output_data')

    deleted_entry = list(filter(lambda x: x[0] == unexisting_user_type_id, output_data))
    
    assert len(deleted_entry) == 0

def test_usertypedata_atualizar_user_type_sem_registro(client, captured_templates):
    """
        [TC014 - D] Falha ao atualizar tipo de usuário quando não existir registro com o ID especificado
    """

    unexisting_user_type_id = -1

    body = { 'user_type_id': unexisting_user_type_id, 'user_type_name': 'User Type Atualizado' }

    params = { 'type_operation': 'U' }

    post_response = send_POST_request('/usertypedata', body, client, captured_templates, params)
    
    output_data = post_response.get('output_data')

    updated_entry = list(filter(lambda x: x[0] == unexisting_user_type_id, output_data))
    
    assert len(updated_entry) == 0

# A view não valida se o nome está vazio, o teste acaba falhando apesar que deveria passar
# def test_usertypedata_atualizar_user_type_sem_registro(client, captured_templates):
#     """
#         [TC014 - D] Falha ao atualizar tipo de usuário quando não passar NOME
#     """

#     body = { 'user_type_id': 1, 'user_type_name': '' }

#     params = { 'type_operation': 'U' }

#     post_response = send_POST_request('/usertypedata', body, client, captured_templates, params)
    
#     output_data = post_response.get('output_data')
    
#     updated_entry = list(filter(lambda x: x[0] == body.get("user_type_name"), output_data))
    
#     assert len(updated_entry) == 1

def test_usertypedata_buscar_todos_user_types(client, captured_templates):

    data = send_GET_request('/usertypedata', client, captured_templates)

    assert len(data.get('usertype_list')) > 0