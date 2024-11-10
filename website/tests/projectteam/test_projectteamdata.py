from utils import send_POST_request
from uuid import uuid4

def test_projectteamdata_inserir_dados_ausentes(client, captured_templates):
    """
    [TC014-A] Verifica se o sistema impede a execução quando faltam dados obrigatórios.
    """

    body = {
        'project_id': '',    
        'user_id': '',       
        'st_user_leader': ''   
    }

    params = {'type_operation': 'A'}

    post_response = send_POST_request('/projectteamdata', body, client, captured_templates, params) # <- O erro acontece aqui porque no próprio send_post_request tem um assert que garante que os campos não estão vazios

    if captured_templates:
        messages = [message for message in captured_templates[0][1].get('_flashes', [])]
        assert ('error', 'Fill out all data to execute transaction!') in messages
    else:
        assert False, "Nenhum template foi renderizado após a requisição POST."

    output_data = post_response.get('output_data')
    assert len(output_data) == 0

def test_projectteamdata_deletar_membro(client, captured_templates):
    """
        [TC014-B] Deletar um membro de um projeto
    """
    
    project_id = "1"
    user_id = "2"
    st_user_leader = "0"

    post_response = send_POST_request('/projectteamdata', {
        'project_id': project_id,
        'user_id': user_id,
        'st_user_leader': st_user_leader
    }, client, captured_templates, { 'type_operation': 'A' })

    output_data = post_response.get('output_data')
    assert len(output_data) > 0
    new_entry_id = output_data[-1][0]

    body = {
        'project_team_id': new_entry_id,
        'project_id': project_id,
        'user_id': user_id,
        'st_user_leader': st_user_leader
    }

    params = { 'type_operation': 'D' }

    post_response = send_POST_request('/projectteamdata', body, client, captured_templates, params)
    
    output_data = post_response.get('output_data')
    deleted_entry = list(filter(lambda x: x[0] == new_entry_id, output_data))

    assert len(deleted_entry) == 0

def test_projectteamdata_inserir_membro(client, captured_templates):
    """
        [TC014-C] Inserir um membro em um time de projeto
    """

    project_id = "1"
    user_id = "2"
    st_user_leader = "0"

    post_response = send_POST_request('/projectteamdata', {
        'project_id': project_id,
        'user_id': user_id,
        'st_user_leader': st_user_leader
    }, client, captured_templates, { 'type_operation': 'A' })

    output_data = post_response.get('output_data')
    assert len(output_data) > 0
    new_entry_id = output_data[-1][0]

    new_entry = list(filter(lambda x: x[0] == new_entry_id, output_data))

    assert len(new_entry) == 1
    assert new_entry[0][0] == new_entry_id
    assert new_entry[0][1] == 'Projeto teste'
    assert new_entry[0][2] == 'NewUser'
    assert new_entry[0][3] == ''

def test_projectteamdata_impedir_duplicidade_membros(client, captured_templates):
    """
        [TC014-D] Impedir duplicidade de membros em um projeto
    """
    
    project_id = "1"
    user_id = "2"
    st_user_leader = "0"

    post_response = send_POST_request('/projectteamdata', {
        'project_id': project_id,
        'user_id': user_id,
        'st_user_leader': st_user_leader
    }, client, captured_templates, { 'type_operation': 'A' })

    output_data = post_response.get('output_data')
    assert len(output_data) > 0
    new_entry_id = output_data[-1][0]

    body = {
        'project_team_id': new_entry_id,
        'project_id': project_id,
        'user_id': user_id,
        'st_user_leader': st_user_leader
    }

    params = { 'type_operation': 'A' }

    post_response = send_POST_request('/projectteamdata', body, client, captured_templates, params)
    
    get_response = client.get(f'/projectteamdata/{project_id}')
    team_members = get_response.get_json()

def test_projectteamdata_atualizar_membro(client, captured_templates):
    """
        [TC014-E] Atualizar um membro em um projeto
    """
    
    project_id = "1"
    user_id = "2"
    st_user_leader = "0"

    post_response = send_POST_request('/projectteamdata', {
        'project_id': project_id,
        'user_id': user_id,
        'st_user_leader': st_user_leader
    }, client, captured_templates, { 'type_operation': 'A' })

    output_data = post_response.get('output_data')
    assert len(output_data) > 0
    new_entry_id = output_data[-1][0]

    body = {
        'project_team_id': new_entry_id,
        'project_id': project_id,
        'user_id': user_id,
        'st_user_leader': '1'
    }

    params = { 'type_operation': 'U' }

    post_response = send_POST_request('/projectteamdata', body, client, captured_templates, params)
    
    output_data = post_response.get('output_data')
    updated_entry = list(filter(lambda x: x[0] == new_entry_id, output_data))

    assert len(updated_entry) == 1
    assert updated_entry[0][0] == new_entry_id
    assert updated_entry[0][3] == 'X'

def test_projectteamdata_determinar_tipo_operacao(client, captured_templates):
    """
        [TC014-F] Determinar o tipo de operação
    """

    # Parâmetros de teste para cada operação: Add (A), Delete (D), Update (U)
    operations = {
        'A': 'Add',
        'D': 'Delete',
        'U': 'Update'
    }

    for operation, expected_type in operations.items():
        params = {
            'type_operation': operation
        }

        captured_templates.clear()

        response = client.get('/projectteamdata', query_string=params)

        assert response.status_code == 200
        assert len(captured_templates) > 0

        template, context = captured_templates[0]

        assert 'type_operation' in context
        assert context['type_operation'] == expected_type

def test_projectteamdata_acesso_sem_project_team_id(client, captured_templates):
    """
        [TC014-G] Tentativa de acessar dados sem project team ID
    """

    params = {
        'project_team_id': ''
    }
    response = client.get('/projectteamdata', query_string=params)

    assert response.status_code == 200

    assert len(captured_templates) > 0
    template, context = captured_templates[0]

    assert 'project_team_id' in context
    assert context['project_team_id'] == ''

    assert context['project_name'] == 0
    assert context['first_name'] == 0
    assert context['st_user_leader'] == 0