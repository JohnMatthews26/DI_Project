from django.test import Client
from io import BytesIO


# def test_function(request, response):
#     c = Client()
#     response = c.post('')
#     print (response.content)
#     return request.method == 'POST', response

def test_function():
    c = Client()
    response = c.get('')
    print (response.content)


    # with open('weinerdogpuppy.jpeg') as fp:
    #     c.post('', {'img': fp})
    # print (response.content)
    # return request.method == 'POST', response
