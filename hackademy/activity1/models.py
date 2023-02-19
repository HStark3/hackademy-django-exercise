from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField()
    description = models.TextField(max_length=250)