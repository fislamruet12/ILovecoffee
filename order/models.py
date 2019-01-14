from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

from datetime import datetime
class DropPost(models.Model):
    owner=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    coffeename=models.CharField(max_length=40,blank=True)
    coffeeamount=models.IntegerField(null=True)
    place=models.CharField(max_length=100,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    created=models.DateField(auto_now=True)


    def __str__(self):
        return self.coffeename
