from django.db import models


# Create your models here.
class Prueba_post(models.Model):
    name = models.CharField(max_length=100)
    action = models.CharField(max_length=250)
    message = models.CharField(max_length=100)