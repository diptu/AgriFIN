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
    gender       = models.CharField(max_length=5)
    address      = models.CharField(max_length=5)

    def __str__(self):
        return self.full_name

class Land(models.Model):
    location        = models.CharField(max_length=120)
    share_price     = models.IntegerField()
    share_quantity  = models.IntegerField()
    fertility_rate  = models.IntegerField()

    def __str__(self):
        return self.location
