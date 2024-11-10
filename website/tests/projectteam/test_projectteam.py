from utils import send_GET_request, send_POST_request
from uuid import uuid4
from unittest.mock import patch

def test_projectteam_Pesquisa_com_valor_valido(client, captured_templates):
    """
        [TC001 - A] Testa o funcionamente com uma pesquisa válida
    """
    valid_search_term = 'Projeto Simulado'

    mock_data = [
        {
            'project_team_id': 1,
            'project_name': 'Projeto Simulado',
            'first_name': 'Jacimar',
            'st_user_leader': 'X'
        }
    ]

    with patch('website.db.get_cursor') as mock_get_cursor:
        mock_cursor = mock_get_cursor.return_value
        mock_cursor.fetchall.return_value = mock_data

        response = client.post('/projectteam', data={'project_search': valid_search_term})
        
        assert response.status_code == 200
        
        template, context = captured_templates[0]
        
        output_data = context.get('output_data')

        assert len(output_data) > 0
        assert output_data == mock_data

def test_projectteam_Pesquisa_com_valor_vazio(client, captured_templates):
    """
        [TC001 - B] Testa o funcionamente com uma pesquisa vazia
    """

    empty_search_term = ''

    response = client.post('/projectteam', data={'project_search': empty_search_term}, follow_redirects=True)
    
    assert response.status_code == 200
    
    template, context = captured_templates[0]
    
    output_data = context.get('output_data')
    assert len(output_data) > 0, "A pesquisa vazia deveria retornar todos os registros de projectteam."


def test_projectteam_verificacao_lider_de_equipe(client, captured_templates):
    """
        [TC001 - C] Verificação de líder de equipe
    """
    
    get_response = send_GET_request('/projectteam', client, captured_templates)
    
    output_data = get_response.get('output_data')
    
    assert len(output_data) > 0, "Nenhuma equipe encontrada para verificação de líderes"

    lideres_incorretos = [entry for entry in output_data if entry[3] == 'X' and not entry[3].strip()]

    assert len(lideres_incorretos) == 0, "Marcação de líder incorreta encontrada na listagem de equipes"

def test_projectteam_Carregamento_ou_pesquisa_sem_banco_de_dados_conectado(client, captured_templates):
    """
        [TC001-D] Verifica o comportamento ao tentar utilizar o sistema sem um banco de dados
    """

    with patch('website.db.get_cursor') as mock_get_cursor:
        mock_get_cursor.side_effect = Exception("Banco de dados inacessível")

        response = client.get('/projectteam')

        assert response.status_code == 500

        response_post = client.post('/projectteam', data={'project_search': 'teste'})

        assert response_post.status_code == 500

