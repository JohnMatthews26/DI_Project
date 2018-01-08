from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
# from PIL import Image
@csrf_exempt
def mainview(request):
    return render(request, 'photo_upload/img.html')
def img(request, photo):
    user_upload = request.POST.get('img', False)
    if user_upload:
        print ('it worked')
    else:
        return render(request, 'photo_upload/mainview.html')
