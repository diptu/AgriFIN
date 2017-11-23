<<<<<<< HEAD
from django.conf import settings
from django.db import models

# Create your models here.
from django.db import models

User = settings.AUTH_USER_MODEL

class Farmer(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name    = models.CharField(max_length=120)
    age          = models.IntegerField()
    # gender       = models.CharField(max_length=6)
    # address      = models.CharField(max_length=120)

    def __str__(self):
        return self.full_name



class Investor(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name    = models.CharField(max_length=120)
    age          = models.IntegerField()
    #gender       = models.CharField(max_length=5)
    #address      = models.CharField(max_length=5)

    def __str__(self):
        return self.full_name

class Land(models.Model):
=======
from django.db import models
from django.contrib.auth.models import AbstractUser


STATUS_CHOICES = (
    (1, ("Farmer")),
    (2, ("Investor")),
    (3, ("Employee")),
)

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

class Land(models.Model):
    owner           = models.ForeignKey(User, limit_choices_to = { 'status': 1})
>>>>>>> 20eb7e3bb2e7cbacc099e1e04e2f96eb6b410657
    location        = models.CharField(max_length=120)
    share_price     = models.IntegerField()
    share_quantity  = models.IntegerField()
    fertility_rate  = models.IntegerField()

    def __str__(self):
        return self.location
