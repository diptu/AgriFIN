# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Person class defination
class Person(models.Model):
    user_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=250)
    birthday =  models.DateField()
    gender  =  models.CharField(max_length=10)
    profile_picture = models.ImageField(max_length=200)
    NID = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    email =models.EmailField()
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=250)
    address = models.CharField(max_length = 500)

# Farmer class defination
class Farmer(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE, primary_key=True)
    user_name = models.CharField(max_length=50)
    NID = models.CharField(max_length=50)
    bank_credentials=models.CharField(max_length=250)


# Investor class defination

class Investor(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE,primary_key=True)
    user_name = models.CharField(max_length=50)
    NID = models.CharField(max_length=50)
    bank_credentials=models.CharField(max_length=250)

# Employee class defination

class Employee(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE, primary_key=True)
    user_name = models.CharField(max_length=50)
    NID = models.CharField(max_length=50)
    branch_id= models.CharField(max_length=250)


# Branch class defination

class Branch(models.Model):
    location = models.CharField(max_length=500)
    number_of_employee = models.DecimalField(decimal_places=0,max_digits=20)


# Land class defination

class Land(models.Model):
    area=models.DecimalField(decimal_places=2,max_digits=20)
    fartility_rate =models.DecimalField(decimal_places=2,max_digits=3)
    location = models.CharField(max_length=500)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    share_price = models.DecimalField(decimal_places=2,max_digits=20)
    share_quantity=models.DecimalField(decimal_places=0,max_digits=5)


# Person Share defination

class Share(models.Model):
        land_id = models.ForeignKey(Land, on_delete=models.CASCADE)
        investor_id= models.ForeignKey(Investor, on_delete=models.CASCADE)
        share_bought=models.DecimalField(decimal_places=2,max_digits=3)
        class Meta:
            unique_together = (('land_id', 'investor_id'),)
