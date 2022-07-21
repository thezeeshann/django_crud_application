from ast import Str
from pyexpat import model
from django.db import models
# Create your models here.

class UserModel(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    image = models.ImageField(blank=True, null=True, upload_to='myimage')

    
