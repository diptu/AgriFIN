from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    STATUS_CHOICES = (
        (1, ("Farmer")),
        (2, ("Investor")),
        (3, ("Employee")),
    )
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)


class Land(models.Model):
    owner           = models.OneToOneField(User, limit_choices_to = { 'status': 1})
    location        = models.CharField(max_length=120)
    share_price     = models.IntegerField()
    share_quantity  = models.IntegerField()
    fertility_rate  = models.IntegerField()

    def __str__(self):
        # return self.owner.username
        return self.location

class Share(models.Model):
    investor = models.ForeignKey(User, limit_choices_to = { 'status': 2})
    land     = models.ForeignKey(Land)
    amount   = models.IntegerField()

    # def __str__(self):
    #     return self.land

# class Branch()
