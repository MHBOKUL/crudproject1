from django.db import models

# Create your models here.
class User (models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField()
    password = models.CharField(max_length=100)
