from django.db import models
from django.db.models.fields import return_None


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    phone = models.CharField(max_length=200)


def __str__(self):
    return self.first_name
