from os import name, path
from django.db import models

# Create your models here.

class Character(models.Model):
    name=models.CharField(max_length=100)
    description= models.CharField(max_length=500)
    path=models.CharField(max_length=200)


    class Meta:
        db_table = 'characters'
