from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainview, name='mainview'),
    path('img', views.img, name='img'),
]
