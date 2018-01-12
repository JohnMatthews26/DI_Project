from django.test import TestCase
from django.test import Client


from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from .views import mainview, img
from io import BytesIO

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()


    # def test_details(self):
    #
    #     request = self.factory.get('')
    #
    #
    #
    #     # Test my_view() as if it were deployed at /customer/details
    #     response = mainview(request)
    #
    #     self.assertEqual(response.status_code, 200)
    #     print (response.content)

    def test_details(self):

        uploaded = SimpleUploadedFile('weinerdogpuppy.jpg', b'file_content', content_type='image/jpeg')
        request = self.factory.post('', {'img': uploaded})



        # Test my_view() as if it were deployed at /customer/details
        response = img(request)

        # self.assertEqual(response.status_code, 200)
        print (response.getvalue())
