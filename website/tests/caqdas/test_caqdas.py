from utils import send_POST_request, send_GET_request

# def test_caqdas_search_empty(client, captured_templates):
#     """
#         Teste TC006-A: Verificar redirecionamento quando a pesquisa está vazia
#     """

#     body = { 'caqdas_search': '' }

#     post_response = send_POST_request('/caqdas', body, client, captured_templates)

#     assert post_response.status_code == 302
#     assert post_response.headers["Location"] == '/caqdas'

def test_caqdas_search(client, captured_templates):
    """
        Teste TC006-B: Verificar pesquisa com resultados
    """
    
    caqdas_name = 'CAQDAS Teste'
    body_create = {
        'caqdas_name': caqdas_name,
        'code_export_type_file': 'text/csv'
    }
    send_POST_request('/caqdasdata', body_create, client, captured_templates, { 'type_operation': 'A' })

    body_search = { 'caqdas_search': caqdas_name }

    post_response = send_POST_request('/caqdas', body_search, client, captured_templates)
    
    # Verifica se a resposta contém o CAQDAS pesquisado
    output_data = post_response.get('output_data')
    assert len(output_data) > 0
    assert any(caqdas_name in item for item in output_data)

    

def test_caqdas_list_all(client, captured_templates):
    """
        Teste TC006-C: Verificar se lista todos os registros com GET
    """

    get_response = send_GET_request('/caqdas', client, captured_templates)

    output_data = get_response.get('output_data')
    assert len(output_data) > 0  