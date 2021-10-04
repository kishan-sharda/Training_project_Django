from django.db import models
from django.db.models.base import Model

# Create your models here.

class watches(models.Model):

    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to = 'pics')
    price = models.IntegerField()

class banners(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'pics')

class user(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    
