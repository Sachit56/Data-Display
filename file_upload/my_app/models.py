from django.db import models

# Create your models here.
class Upload(models.Model):
    upload =models.FileField(upload_to='uploads/')

class Datas(models.Model):
    state = models.CharField(max_length=100)
    dpd = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False) 
    account = models.CharField(max_length=150)
    pin = models.IntegerField()
