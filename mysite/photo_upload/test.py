from django.test import Client


def test_function(request, response):
    return request.method == 'POST', response
