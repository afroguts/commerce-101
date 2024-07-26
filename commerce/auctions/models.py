from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField(max_length=70)

    pass

class Product(models.Model):
   P_name = models.CharField(max_length=100)
   P_descr = models.CharField(max_length=700)
   P_bid = models.IntegerField()
   P_image = models.CharField(max_length=700)
   User = models.ForeignKey(User, related_name='item_name', on_delete=models.CASCADE)

   pass



class comments(models.Model):
    comment = models.CharField(max_length=700)
    pass
