def send_GET_request(url, client, captured_templates, params=None):
    client.get(url, query_string=params)

    assert len(captured_templates) > 0

    template, data = captured_templates[-1]

    return data

def send_POST_request(url, body, client, captured_templates, params=None):
    client.post(url, data=body, query_string=params, follow_redirects=True)

    assert len(captured_templates) > 0

    template, data = captured_templates[-1]

    return data

def encontra_item_na_lista(lista, index_da_tupla, campo):
    """
        Procura um item dentro de uma lista de tuplas

        As duas funções acima de requisição HTTP retorna uma lista com os dados em formato de tupla, como:
        (1, 'Nome da Linha de Pesquisa', 1, 'Nome do Usuário') => (research_line_id, research_line_name, user_id_log, user_name_log)

        Para saber a ordem de uma tupla não é muito intuitivo. O jeito mais rápido é fazer um `assert` que force um erro como `assert list == 1`
        Isso por que o pytest irá printar as tuplas que estiverem na lista e será possível ver a ordem e escolher o index necessário
    """

    result = list(filter(lambda x: x[index_da_tupla] == campo, lista))

    assert len(result) == 1

    return result[0]