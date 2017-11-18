
from django.forms import ModelForm
from django.db import models



# Person table defination

class Person(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    full_name = models.CharField(max_length=250)
    birthday =  models.DateField(null=True)
    gender  =  models.CharField(max_length=10)
    profile_picture = models.ImageField(max_length=200)
    NID = models.CharField(max_length=50)
    email =models.EmailField()
    qualification = models.CharField(max_length=250,default="HSC")
    mobile_no = models.CharField(max_length=250)
    address = models.CharField(max_length = 500)
    bank_credentials=models.CharField(max_length=250)
    title = models.CharField(max_length=10)
    class Meta:
        unique_together = (('username', 'password'),)

    def get(self):
        return self.full_name+' '+self.gender+' '+self.email+' '+self.qualification+' '+self.address+' '+self.title

    def __str__(self):

        return self.full_name+' '+self.gender+' '+self.email+' '+self.address+' '+self.title

## Farmer table defination
class Farmer(models.Model):


    farmer_obj =Person.objects.filter(title='Farmer')

    def get_info(self):
        return self.farmer_obj.get()

    def __str__(self):
        return self.full_name

class Investor(models.Model):
    #title=ModelChoiceField()
    # models.ForeignKey(Farmer, on_delete=models.CASCADE)

    investor_obj =Person.objects.filter(title='Investor')
    def get_info(self):
        return self.investor_obj.get()
    def __str__(self):
        return self.full_name

class Employee(models.Model):
    #title=ModelChoiceField()
    # models.ForeignKey(Farmer, on_delete=models.CASCADE)
    employee_obj =Person.objects.filter (title='employee')
    def get_info(self):
        return self.employee_obj.get()

    def __str__(self):
        return self.full_name






#class Farmer(models.Model):
 #   full_name    = models.CharField(max_length=120)
  #  age          = models.IntegerField()
   # gender       = models.CharField(max_length=6)
    #address      = models.CharField(max_length=120)

   # def __str__(self):
    #    return self.full_name


#class Investor(models.Model):
 #   full_name    = models.CharField(max_length=120)
  #  age          = models.IntegerField()
   # gender       = models.CharField(max_length=5)
    #address      = models.CharField(max_length=5)

    #def __str__(self):
     #   return self.full_name


class Land(models.Model):
    location        = models.CharField(max_length=120)
    share_price     = models.IntegerField()
    share_quantity  = models.IntegerField()
    fertility_rate  = models.IntegerField()

    def __str__(self):
        return self.location
