from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete = models.CASCADE, null=True,
    
    )
#    name = models.CharField(max_length=100)
    profile_picture = models.ImageField()
    description = models.TextField(max_length=250)