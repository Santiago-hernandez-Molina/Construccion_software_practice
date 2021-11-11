from os import name
from django import db
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=3000)
    video = models.FileField(upload_to="")

    class Meta:
        db_table = "categories"


class CaseStudy(models.Model):
    name = CharField(max_length=100)
    description = models.CharField(max_length=200)
    path = models.FileField(upload_to="")
    projectObjective = models.CharField(max_length=2000)
    clientBenefit = models.CharField(max_length=2000)
    projectResult = models.CharField(max_length=2000)
    projectBackground = models.CharField(max_length=3000)
    category = models.ForeignKey(Category, on_delete=CASCADE)

    class Meta:
        db_table = "caseStudies"
