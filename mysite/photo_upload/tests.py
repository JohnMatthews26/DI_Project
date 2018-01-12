from django.test import TestCase
from django.test import Client


from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from .views import mainview, img
from io import BytesIO

class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):

        uploaded = SimpleUploadedFile('weinerdogpuppy.jpg', b'file_content', content_type='image/jpeg')
        request = self.factory.post('', {'img': uploaded})
        response = img(request)
        print (response.getvalue())
