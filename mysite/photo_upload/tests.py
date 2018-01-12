from django.test import TestCase
from django.test import Client

def test_function():
    c = Client()
    response = c.get('')
    return response.content
