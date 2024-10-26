from uuid import uuid4

from utils import send_GET_request, send_POST_request

def test_researchlinedata_adicionar_nova_linha_de_pesquisa(client, captured_templates):
    """
        [TC011 - A] Adicionar nova Linha de Pesquisa com os dados enviados
    """
    # Arrange #
    get_response = send_GET_request('/researchline', client, captured_templates)

    current_total_entries = len(get_response.get('output_data'))
        
    body = { 'research_line_name': 'Linha de Pesquisa Teste' }

    params = { 'type_operation': 'A' }

    # Act #
    post_response = send_POST_request('/researchlinedata', body, client, captured_templates, params)

    # Assert #
    output_data = post_response.get('output_data')

    assert len(output_data) == current_total_entries + 1

def test_researchlinedata_atualizar_linha_de_pesquisa(client, captured_templates):
    """
        [TC011 - B] Atualizar o nome de uma Linha de Pesquisa com os dados enviados
    """

    # Arrange #
    research_line_name = 'Linha de Pesquisa para Atualizar ' + uuid4().hex

    post_response = send_POST_request('/researchlinedata', { 'research_line_name': research_line_name }, client, captured_templates, { 'type_operation': 'A' })

    research_lines = post_response.get('output_data')

    assert len(research_lines) > 0

    # Retorna um array com tuplas no seguinte formato: (15, 'Linha de Pesquisa', 2, 'Teste') A ordem segue a ordem encontrada no model equivalente do arquivo model.py
    new_entry = list(filter(lambda x: x[1] == research_line_name, research_lines))
    # O primeiro index 0 corresponde ao único item retornado pela linha anterior e o segundo se refere primeiro item da tupla, que é o ID
    new_entry_id = new_entry[0][0]
        
    body = { 'research_line_id': new_entry_id, 'research_line_name': 'Linha de Pesquisa Atualizada' }

    params = { 'type_operation': 'U' }

    # Act #
    post_response = send_POST_request('/researchlinedata', body, client, captured_templates, params)

    # Assert #
    output_data = post_response.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[0] == new_entry_id, output_data))
    updated_entry_id = updated_entry[0][0]

    assert updated_entry_id == new_entry_id

    assert updated_entry[0][1] == body['research_line_name']

def test_researchlinedata_nao_atualizar_linha_de_pesquisa_sem_registro(client, captured_templates):
    """
        [TC011 - C] Falha ao atualizar uma Linha de Pesquisa quando não existir registro com o ID especificado
    """

    # Arrange #
    unexisting_research_line_id = -1

    body = { 'research_line_id': unexisting_research_line_id, 'research_line_name': 'Linha de Pesquisa Atualizada' }

    params = { 'type_operation': 'U' }

    # Act #
    post_response = send_POST_request('/researchlinedata', body, client, captured_templates, params)

    # Assert #
    output_data = post_response.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[0] == unexisting_research_line_id, output_data))

    assert len(updated_entry) == 0

def test_researchlinedata_deletar_linha_de_pesquisa(client, captured_templates):
    """
        [TC011 - D] Excluir Linha de Pesquisa com o ID especificado
    """

    # Arrange #
    research_line_name =  'Linha de Pesquisa para Deletar ' + uuid4().hex

    post_response = send_POST_request('/researchlinedata', { 'research_line_name': research_line_name }, client, captured_templates, { 'type_operation': 'A' })

    research_lines = post_response.get('output_data')

    assert len(research_lines) > 0

    # Retorna um array com tuplas no seguinte formato: (15, 'Linha de Pesquisa', 2, 'Teste') A ordem segue a ordem encontrada no model equivalente do arquivo model.py
    new_entry = list(filter(lambda x: x[1] == research_line_name, research_lines))
    # O primeiro index 0 corresponde ao único item retornado pela linha anterior e o segundo se refere primeiro item da tupla, que é o ID
    new_entry_id = new_entry[0][0]
        
    body = { 'research_line_id': new_entry_id }

    params = { 'type_operation': 'D' }

    # Act #
    post_response = send_POST_request('/researchlinedata', body, client, captured_templates, params)

    # Assert #
    output_data = post_response.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[0] == new_entry_id, output_data))

    assert len(updated_entry) == 0
    
def test_researchlinedata_nao_deletar_linha_de_pesquisa_sem_registro(client, captured_templates):
    """
        [TC011 - E] Falha ao deletar uma Linha de Pesquisa quando não existir registro com o ID especificado
    """

    # Arrange #
    unexisting_research_line_id = -1

    body = { 'research_line_id': unexisting_research_line_id }

    params = { 'type_operation': 'D' }

    # Act #
    post_response = send_POST_request('/researchlinedata', body, client, captured_templates, params)

    # Assert #
    output_data = post_response.get('output_data')

    assert len(output_data) > 0

    updated_entry = list(filter(lambda x: x[0] == unexisting_research_line_id, output_data))

    assert len(updated_entry) == 0

def test_researchlinedata_buscar_dados_das_linhas_de_pesquisas(client, captured_templates):
    """
        [TC011 - F] Retornar todas as linhas de pesquisa salvas na base de dados
    """
    args = {
        'research_line_id': '0',
        'research_line_name': 'Novo Nome de Linha de Pesquisa',
        'type_operation': 'D'
    }

    data = send_GET_request('/researchlinedata', client, captured_templates, args)

    assert data.get('type_operation') == 'Delete'
    assert data.get('research_line_id') == args['research_line_id']
    assert data.get('research_line_name') == args['research_line_name']

def test_researchlinedata_buscar_dados_das_linhas_de_pesquisas_vazio(client, captured_templates):
    """
        [TC011 - G] Retornar todas as linhas de pesquisa salvas na base de dados
    """
    args = { }

    data = send_GET_request('/researchlinedata', client, captured_templates, args)

    assert data.get('type_operation') == 'Add'