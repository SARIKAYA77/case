from django.db import models
from django.db.models.signals import post_save, post_delete
# Create your models here.


class Data(models.Model):
    text = models.TextField()
    label = models.TextField()


def save_data(sender, instance, **kwargs):
    print(instance.text)
    print(instance.label)


def delete_data(sender, instance, **kwargs):
    print("data deleted")


post_save.connect(save_data, sender=Data)
post_delete.connect(save_data, sender=Data)
