from django.db import models
from .utility import generate_account_number


# Create your models here.

class Account(models.Model):
    account_number = models.CharField(max_length=10, default=generate_account_number, unique=True, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    pin = models.CharField(max_length=4)
