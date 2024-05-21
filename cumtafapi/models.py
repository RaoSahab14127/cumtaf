
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import customUserManager
class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=100, unique=True)
    age = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = customUserManager()

