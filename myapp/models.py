from django.db import models

class user(models.Model):
    username = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)