from os import name, path
from django.db import models

# Create your models here.

class Character(models.Model):
    name=models.CharField(max_length=200)
    description= models.CharField(max_length=1000)
    path=models.FileField(upload_to="")
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = 'characters'
