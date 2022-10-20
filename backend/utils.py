import json


def parse_request(request):
    return json.loads(request.body.decode('utf-8'))
