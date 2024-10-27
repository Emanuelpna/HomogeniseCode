from utils import send_GET_request, send_POST_request
from uuid import uuid4

def test_projectdata_validacao_campos_obrigatorios(client, captured_templates):
    get_response = send_GET_request('/projectresearch', client, captured_templates)
    current_total_entries = len(get_response.get('output_data'))
    data = send_POST_request('/projectdata', {'project_id': '', 'project_name': '', 'project_description': '', 'research_line_id': ''}, client, captured_templates, {'type_operation' : 'A'})
    output_data = data.get('output_data')
    assert len(output_data) == current_total_entries

def test_projectdata_cadastro_projeto(client, captured_templates):
    research_line_name = 'Teste cadastro projeto' + uuid4().hex
    research_line_response = send_POST_request('/researchlinedata', {'research_line_name': research_line_name}, client, captured_templates, {'type_operation' : 'A'})
    research_lines = research_line_response.get('output_data')
    new_researchline = list(filter(lambda x: x[1] == research_line_name, research_lines))
    data = send_POST_request('/projectdata', {'project_name': 'Projeto teste', 'project_description': 'Projeto criado para teste de função', 'research_line_id': new_researchline[0][0]}, client, captured_templates, {'type_operation' : 'A'})
    output_data = data.get('output_data')
    assert type(output_data) == list
    lista_projeto = list(filter(lambda x: x[2] == 'Projeto teste', output_data))
    assert len(lista_projeto) > 0

def test_projectdata_atualizar_projeto(client, captured_templates):
    research_line_name = 'Teste atualizar cadastro projeto' + uuid4().hex
    research_line_response = send_POST_request('/researchlinedata', {'research_line_name': research_line_name}, client, captured_templates, {'type_operation' : 'A'})
    research_lines = research_line_response.get('output_data')
    new_researchline = list(filter(lambda x: x[1] == research_line_name, research_lines))
    # data = send_POST_request('/projectdata', {'project_name': 'Projeto teste', 'project_description': 'Projeto criado para teste de função', 'research_line_id': new_researchline[0][0]}, client, captured_templates, {'type_operation' : 'A'})

    project_name = 'Teste atualizar cadastro projeto' + uuid4().hex
    project_response = send_POST_request('/projectdata', {'project_name': project_name, 'project_description': 'Projeto criado para teste de função', 'research_line_id': new_researchline[0][0]}, client, captured_templates, {'type_operation' : 'A'})
    projects = project_response.get('output_data')
    new_project = list(filter(lambda x: x[2] == project_name, projects))
    
    data = send_POST_request('/projectdata', {'project_id': new_project[0][0], 'project_name': 'Projeto teste atualizado', 'project_description': 'Projeto criado para teste de função de atualização de projeto', 'research_line_id': new_researchline[0][0]}, client, captured_templates, {'type_operation' : 'U'})

    output_data = data.get('output_data')
    assert type(output_data) == list
    lista_projeto = list(filter(lambda x: x[2] == 'Projeto teste atualizado', output_data))
    assert len(lista_projeto) > 0

def test_projectdata_buscar_projeto(client, captured_templates):
    args = {
        'project_name': 'Projeto teste', 
        'project_description': 'Projeto criado para teste de função' 
        }
    data = send_GET_request('/projectdata', client, captured_templates, args)
    assert data.get('type_operation') == 'Add'
    assert data.get('project_name') == args['project_name']
    assert data.get('project_description') == args['project_description']

# def test_projectdata_buscar_linha_pesquisa(client, captured_templates):
#     research_line_name = 'Teste pesquisar linha de projeto' + uuid4().hex
#     research_line_response = send_POST_request('/researchlinedata', {'research_line_name': research_line_name}, client, captured_templates, {'type_operation' : 'A'})
#     research_lines = research_line_response.get('output_data')
#     new_researchline = list(filter(lambda x: x[1] == research_line_name, research_lines))
#     project_response = send_POST_request('/projectdata', {'project_name': 'Projeto teste', 'project_description': 'Projeto criado para teste de função', 'research_line_id': new_researchline[0][0]}, client, captured_templates, {'type_operation' : 'A'})

#     project_lines = project_response.get('output_data')
    
#     project_line = list(filter(lambda x: x[2] == 'Projeto teste', project_lines))
    

#     args = {
#         'project_id': project_line[0][0],
#         'project_name': 'Projeto teste', 
#         'project_description': 'Projeto criado para teste de função',
#         'research_line_id': new_researchline[0][0]
#         }
#     data = send_GET_request('/projectdata', client, captured_templates, args)
    

#     assert data.get('project_name') == args['project_name']
#     assert data.get('project_description') == args['project_description']
#     assert data.get('researchline_name') == research_line_name

def test_projectdata_listar_projeto(client, captured_templates):
    get_response = send_GET_request('/researchline', client, captured_templates)
    current_total_entries = len(get_response.get('output_data'))

    args = {
        'project_name': 'Projeto teste', 
        'project_description': 'Projeto criado para teste de função' 
        }
    data = send_GET_request('/projectdata', client, captured_templates, args)
    assert len(data.get('researchline_list')) == current_total_entries

# def test_projectdata_nao_deletar_projeto_com_time(client, captured_templates):
#     research_line_name = 'Teste para nao deletar projeto' + uuid4().hex
#     research_line_response = send_POST_request('/researchlinedata', {'research_line_name': research_line_name}, client, captured_templates, {'type_operation' : 'A'})
#     research_lines = research_line_response.get('output_data')
#     new_researchline = list(filter(lambda x: x[1] == research_line_name, research_lines))
    
#     # assert new_researchline[0][0] == 1
#     project_name = 'Teste para nao deletar projeto' + uuid4().hex
#     project_response = send_POST_request('/projectdata', {'project_name': project_name, 'project_description': 'Projeto criado para teste de função', 'research_line_id': new_researchline[0][0]}, client, captured_templates, {'type_operation' : 'A'})
#     projects = project_response.get('output_data')
#     new_project = list(filter(lambda x: x[2] == project_name, projects))
#     # assert new_project == 1
#     send_POST_request('/projecttimedata', {'project_id': new_project[0][0], 'user_id': '1', 'st_user_leader': '1'}, client, captured_templates, {'type_operation' : 'A'})

#     data = send_POST_request('/projectdata', {'project_id': new_project[0][0]}, client, captured_templates, {'type_operation' : 'D'})

#     output_data = data.get('output_data')
#     assert type(output_data) == 1
#     lista_projeto = list(filter(lambda x: x[0] == new_project[0][0], output_data))
#     assert len(lista_projeto) > 0

def test_projectdata_deletar_projeto(client, captured_templates):
    research_line_name = 'Teste para deletar projeto' + uuid4().hex
    research_line_response = send_POST_request('/researchlinedata', {'research_line_name': research_line_name}, client, captured_templates, {'type_operation' : 'A'})
    research_lines = research_line_response.get('output_data')
    new_researchline = list(filter(lambda x: x[1] == research_line_name, research_lines))

    project_name = 'Teste para deletar projeto' + uuid4().hex
    project_response = send_POST_request('/projectdata', {'project_name': project_name, 'project_description': 'Projeto criado para teste de função', 'research_line_id': new_researchline[0][0]}, client, captured_templates, {'type_operation' : 'A'})
    projects = project_response.get('output_data')
    new_project = list(filter(lambda x: x[2] == project_name, projects))
    
    data = send_POST_request('/projectdata', {'project_id': new_project[0][0]}, client, captured_templates, {'type_operation' : 'D'})

    output_data = data.get('output_data')
    assert type(output_data) == list
    lista_projeto = list(filter(lambda x: x[0] == new_project[0][0], output_data))
    assert len(lista_projeto) == 0