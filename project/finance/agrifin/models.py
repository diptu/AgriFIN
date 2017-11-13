from django.db import models

class Farmer(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Investor(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
