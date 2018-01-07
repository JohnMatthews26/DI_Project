from django.db import models

# Create your models here.
class PhotoUpload(models.Model):
    photo = models.FileField(upload_to='PhotoUpload/')
