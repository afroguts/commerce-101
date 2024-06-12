from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField(max_length=70)

    pass

class auction_listings(models.Model):
   name = models.CharField(max_length=100) 
   description = models.CharField(max_length=700)


   pass


class bids(models.Model):
    reference = models.IntegerField()
    bid = models.IntegerField()
    pass

class comments(models.Model):
    comment = models.CharField(max_length=700)
    pass