from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File
from . import test
# from PIL import Image
@csrf_exempt
def mainview(request):
    print (request)
    return render(request, 'photo_upload/mainview.html')
def img(request):
    photo = request.FILES
    # print (test.test_function(request)
    return HttpResponse(photo.getlist('img')[0].read(), content_type="image/jpeg")
