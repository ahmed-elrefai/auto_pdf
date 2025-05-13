from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(AbstractUser):
    premium_user = models.BooleanField(default=False)   #After payment
