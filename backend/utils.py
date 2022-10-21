def parse_request(request):
    print(request.data)
    return dict(request.data)
