from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import *
from datetime import date


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True, default='None')
    phone = models.CharField(max_length=50, blank=True, null=True)
    car_model = models.CharField(max_length=50, blank=True, null=True)
    car_number = models.CharField(max_length=50, blank=True, null=True)
    vin = models.CharField(max_length=50, blank=True, null=True)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Work(models.Model):
    work = models.ForeignKey(User, on_delete = models.CASCADE)
    work_name = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(default=date.today, null=True, blank=True)



# Create your models here.
