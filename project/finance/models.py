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
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)


    # def __str__(self):
    #     return self.land



class Budget(models.Model):
    # land             = models.OneToOneField(Land)
    # crop             = models.OneToOneField(Crop)
    worker_fee       = models.DecimalField( max_digits=20, decimal_places=2)
    irrigation_fee   = models.DecimalField( max_digits=20, decimal_places=2)
    other_cost       = models.DecimalField( max_digits=20, decimal_places=2)
    # def total_cost(self):
    #     return  (self.worker_fee + self.irrigation_fee + self.other_cost)
    def __str__(self):
        return str(self.worker_fee + self.irrigation_fee + self.other_cost)

class Branch(models.Model):
    branch_location =   models.CharField(max_length=120, null=False , blank=False)
    no_of_employee  =   models.IntegerField()

    def __str__(self):
        # return self.owner.username
        return self.branch_location


class Land(models.Model):
    owner           = models.ForeignKey(User, limit_choices_to = { 'status': 1})
    budget          = models.OneToOneField(Budget)
    location        = models.CharField(max_length=120)
    share_price     = models.IntegerField()
    share_quantity  = models.IntegerField()
    fertility_rate  = models.IntegerField()
    branch          = models.ForeignKey(Branch, null=True, blank=True)
    total_share     = models.IntegerField()
    share_sold      = models.IntegerField(default=0)

    def __str__(self):
        # return self.owner.username
        return self.location

class Share(models.Model):
    investor     = models.ForeignKey(User, limit_choices_to = { 'status': 2})
    land         = models.ForeignKey(Land)
    amount       = models.IntegerField()
    percentage   = models.IntegerField(null = True)

    def __str__(self):
        return self.investor.username



class Fertilizer(models.Model):

    fertilizer_name  = models.CharField(max_length=50)
    unit_price       = models.IntegerField(null=False)
    amount_per_sqft  = models.DecimalField( max_digits=20, decimal_places=2)

    def __str__(self):
        return self.fertilizer_name

class Crop(models.Model):
    crop_name        = models.CharField(max_length=50,null=False,blank=False)
    unit_price       = models.IntegerField(null=False)
    amount_per_sqft  = models.DecimalField( max_digits=20, decimal_places=2)
    fertilizer_name  = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)

    def __str__(self):
        return self.crop_name


class Revenue(models.Model):
    total_revenue   = models.DecimalField( max_digits=20, decimal_places=2)
    budget          = models.OneToOneField(Budget)




    def get_total_revenue(self):
       return  (self.total_revenue - self.budget.total_cost() )
