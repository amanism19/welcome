from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    userStatus = models.BooleanField(null=False,blank=False)
    creatorStatus = models.BooleanField(null=False,blank=False)
    buyerStatus = models.BooleanField(null=False,blank=False)