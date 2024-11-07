from utils import send_POST_request, send_GET_request
from uuid import uuid4

def test_caqdasdata_adicionar_novo_caqdas(client, captured_templates):
    get_response = send_GET_request('/caqdasdata', client, captured_templates)

    current_total_entries = len(get_response.get('output_data'))

    body = { 
        'caqdas_name' : 'Nome do CAQDAS',
        'code_export_type_file' : 'text/csv' }

    params = { 'type_operation' : 'A' }

    post_response = send_POST_request('/caqdasdata', body, client, captured_templates, params)

    output_data = post_response.get('output_data')

    assert len(output_data) == current_total_entries + 1

def test_caqdasdata_atualizar_caqdas(client, captured_templates):

    caqdas_name = 'CAQDAS para Atualizar ' + uuid4().hex

    body_create = {
        'caqdas_name': caqdas_name,
        'code_export_type_file': 'text/csv'
    }

    post_response = send_POST_request('/caqdasdata', body_create, client, captured_templates, { 'type_operation': 'A' })
    
    caqdas_entries = post_response.get('output_data')

    new_entry = list(filter(lambda x: x[1] == caqdas_name, caqdas_entries))

    new_entry_id = new_entry[0][0]
    
    body_update = {
        'caqdas_id': new_entry_id,
        'caqdas_name': 'NOVO Nome do CAQDAS',
        'code_export_type_file': 'text/csv'
    }
    params = { 'type_operation': 'U' }

    post_response = send_POST_request('/caqdasdata', body_update, client, captured_templates, params)
    
    output_data = post_response.get('output_data')

    updated_entry = list(filter(lambda x: x[0] == new_entry_id, output_data))
    
    assert updated_entry[0][1] == body_update['caqdas_name']

def test_caqdasdata_deletar_caqdas(client, captured_templates):
    caqdas_name = 'CAQDAS para Deletar' + uuid4().hex

    body_create = {
        'caqdas_name': caqdas_name,
        'code_export_type_file': 'text/csv'
    }

    post_response = send_POST_request('/caqdasdata', body_create, client, captured_templates, { 'type_operation': 'A' })
    
    caqdas_entries = post_response.get('output_data')
    new_entry = list(filter(lambda x: x[1] == caqdas_name, caqdas_entries))
    new_entry_id = new_entry[0][0]
    
    body_delete = { 'caqdas_id': new_entry_id }
    params = { 'type_operation': 'D' }

    post_response = send_POST_request('/caqdasdata', body_delete, client, captured_templates, params)
    
    output_data = post_response.get('output_data')
    deleted_entry = list(filter(lambda x: x[0] == new_entry_id, output_data))
    
    assert len(deleted_entry) == 0

def test_caqdasdata_nao_atualizar_caqdas_sem_registro(client, captured_templates):

    unexisting_caqdas_id = -1
    body = {
        'caqdas_id': unexisting_caqdas_id,
        'caqdas_name': 'CAQDAS Atualizado',
        'code_export_type_file': 'text/csv'
    }
    params = { 'type_operation': 'U' }

    post_response = send_POST_request('/caqdasdata', body, client, captured_templates, params)
    
    output_data = post_response.get('output_data')
    updated_entry = list(filter(lambda x: x[0] == unexisting_caqdas_id, output_data))
    
    assert len(updated_entry) == 0

def test_caqdasdata_nao_deletar_sem_registro(client, captured_templates):
    unexisting_caqdas_id = -1
    body = { 'caqdas_id': unexisting_caqdas_id }
    params = { 'type_operation': 'D' }

    post_response = send_POST_request('/caqdasdata', body, client, captured_templates, params)
    
    output_data = post_response.get('output_data')
    deleted_entry = list(filter(lambda x: x[0] == unexisting_caqdas_id, output_data))
    
    assert len(deleted_entry) == 0

def test_caqdasdata_buscar_todos_caqdas(client, captured_templates):
    data = send_GET_request('/caqdasdata', client, captured_templates)

    assert len(data.get('output_data')) > 0