from django.db import models

import random
# Create your models here.


def random_string():
      return str(random.randint(1000000, 99999999))

class Product(models.Model):
   name = models.CharField(max_length=255)
   price = models.IntegerField()
   description = models.TextField()
   buy_order = models.CharField(default=random_string, max_length=100)
   session_id = models.CharField(default=random_string, max_length=100)

   def __str__(self):
        return self.name

