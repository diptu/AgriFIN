from django.db import models

#Farmer class defination
class Farmer(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    full_name = models.CharField(max_length=250,null=True)
    birthday =  models.DateField(null=True)
    gender  =  models.CharField(max_length=10,null=True)
    profile_picture = models.ImageField(max_length=200,null=True)
    NID = models.CharField(max_length=50,null=True)
    email =models.EmailField(null=True)
    qualification = models.CharField(max_length=250,null=True)
    address = models.CharField(max_length = 500,null=True)
    bank_credentials=models.CharField(max_length=250,null=True)


#Investor class defination
class Investor(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    full_name = models.CharField(max_length=250,null=True)
    birthday =  models.DateField(null=True)
    gender  =  models.CharField(max_length=10,null=True)
    profile_picture = models.ImageField(max_length=200,null=True)
    NID = models.CharField(max_length=50,null=True)
    email =models.EmailField(null=True)
    qualification = models.CharField(max_length=250,null=True)
    address = models.CharField(max_length = 500,null=True)
    bank_credentials=models.CharField(max_length=250,null=True)

#Employee class defination
class Employee(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    full_name = models.CharField(max_length=250,null=True)
    birthday =  models.DateField(null=True)
    gender  =  models.CharField(max_length=10,null=True)
    profile_picture = models.ImageField(max_length=200,null=True)
    NID = models.CharField(max_length=50,null=True)
    email =models.EmailField(null=True)
    qualification = models.CharField(max_length=250,null=True)
    address = models.CharField(max_length = 500,null=True)

#Branch class defination
class Branch(models.Model):
    location = models.CharField(max_length=500)
    number_of_employee = models.DecimalField(decimal_places=0,max_digits=20)

#Land class defination
class Land(models.Model):
    area=models.DecimalField(decimal_places=2,max_digits=20)
    fartility_rate =models.DecimalField(decimal_places=2,max_digits=3)
    location = models.CharField(max_length=500)
    farmer_id = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    share_price = models.DecimalField(decimal_places=2,max_digits=20)
    share_quantity=models.DecimalField(decimal_places=0,max_digits=5)

class Share(models.Model):
    land_id = models.ForeignKey(Land, on_delete=models.CASCADE)
    investor_id= models.ForeignKey(Investor, on_delete=models.CASCADE)
    share_bought=models.DecimalField(decimal_places=2,max_digits=3)
    class Meta:
        unique_together = (('land_id', 'investor_id'),)

#CROP class defination
class Crop(models.Model):
    crop_name=models.CharField(max_length=500)
    unit_price=models.DecimalField(decimal_places=2,max_digits=20)
    amount_per_sqft=models.DecimalField(decimal_places=2,max_digits=20)


#FERTILIZER(dependent on CROP):

class Fertilizer(models.Model):
    fertilizer_name=models.CharField(max_length=500,primary_key=True)
    crop_name = models.ForeignKey(Crop, on_delete=models.CASCADE)
    unit_price=models.DecimalField(decimal_places=2,max_digits=20)
    amount_per_sqft=models.DecimalField(decimal_places=2,max_digits=20)

#REVENUE(dependent on LAND):

class Revenue(models.Model):
    land_id = models.ForeignKey(Land, on_delete=models.CASCADE)
    total_cost=models.DecimalField(decimal_places=2,max_digits=20)
    total_revenue=models.DecimalField(decimal_places=2,max_digits=20)

#BUDGET(dependent on LAND):_

class Budget(models.Model):
    land_id = models.ForeignKey(Land, on_delete=models.CASCADE)
    crop_id= models.ForeignKey(Crop, on_delete=models.CASCADE)
    worker_fee=models.DecimalField(decimal_places=2,max_digits=20)
    irrigation_fees=models.DecimalField(decimal_places=2,max_digits=20)
    other_cost=models.DecimalField(decimal_places=2,max_digits=20)
    total_cost=models.DecimalField(decimal_places=2,max_digits=20)
