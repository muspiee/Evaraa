from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Customuser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', default='def.png')
    email = models.EmailField(max_length=40, unique=True)
    phone_number = models.TextField(max_length=50, unique=True)
