


def test_function(request, response):
    return request.method == 'POST', response
