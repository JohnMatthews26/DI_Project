from django.db import models

# Create your models here.
class Photo(models.Model):
    photo = models.FileField(upload_to='photo')
