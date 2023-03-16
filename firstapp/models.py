from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.BooleanField()
    