from django.test import Client



def test_function(request, response):
    c = Client()
    response = c.get('')
    print (response.content)
    return request.method == 'POST', response
