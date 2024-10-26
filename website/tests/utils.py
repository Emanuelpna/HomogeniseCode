import inspect

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