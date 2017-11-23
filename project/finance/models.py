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
    location        = models.CharField(max_length=120)
    share_price     = models.IntegerField()
    share_quantity  = models.IntegerField()
    fertility_rate  = models.IntegerField()

    def __str__(self):
        return self.location
