from django.db import models

# Create your models here.
class Data(models.Model):
    text = models.TextField()
    label = models.TextField()
    