from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField(max_length=70)

    pass

class Auction_item(models.Model):
   item_name = models.CharField(max_length=100)
   description = models.CharField(max_length=700)
   User = models.ForeignKey(User, related_name='item_name', on_delete=models.CASCADE)

   pass


class bids(models.Model):
    bid = models.IntegerField()
    auction_item= models.ForeignKey(Auction_item, related_name='bid', on_delete=models.CASCADE)
    pass

class comments(models.Model):
    comment = models.CharField(max_length=700)
    pass
