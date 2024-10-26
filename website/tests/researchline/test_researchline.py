from utils import send_GET_request

def test_request_researchline(client, captured_templates):
    data = send_GET_request('/researchline', client, captured_templates)

    output_data = data.get('output_data')

    assert len(output_data) > 0