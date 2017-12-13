from django import forms
from django.contrib.auth.forms import UserCreationForm
from finance.models import *
from django.contrib.auth import get_user_model
User = get_user_model()

# class SignUpForm(UserCreationForm):
#     age = forms.IntegerField()
#
#     class Meta:
#         model = User
#         fields = ('username', 'age', 'password1', 'password2', )

# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
class LandUpdate(forms.Form):
    owner          = forms.ModelChoiceField(queryset=User.objects.filter(status=1))
    location       = forms.CharField()
    share_price    = forms.IntegerField()
    share_quantity = forms.IntegerField()
    fertility_rate = forms.DecimalField(min_value = 0.0, max_value = 100.0)
    worker_fee     = forms.IntegerField()
    other_cost     = forms.IntegerField()
    irrigation_fee = forms.IntegerField()

    # class Meta:
    #     model = Land




    #     fields = ('land_id', 'user_id','buy_share',)
class ProfileUpdate(forms.Form):
    #first_name       = forms.CharField(required=False)
    #last_name        = forms.CharField(required=False)
    bio              = forms.CharField(required=False)
    location         = forms.CharField(required=False)
    email            = forms.EmailField(required=False)

    #share_quantity = forms.IntegerField()
    #fertility_rate = forms.DecimalField(min_value = 0.0, max_value = 100.0)
    #worker_fee     = forms.IntegerField()
    #other_cost     = forms.IntegerField()
    #irrigation_fee = forms.IntegerField()
    def __init__(self, *args, **kwargs):
        #self.user = kwargs.pop('user')   # the blog entry instance
        super().__init__(*args, **kwargs)

    def save(self):
        #user = super().save(commit=False)
        #comment.entry = self.entry
        #user.save()
        return self


class BuyShare(forms.Form):
    quantity = forms.IntegerField()

    class Meta:
        model = Land
        fields = ('land_id', 'user_id','buy_share',)


STATUS_CHOICES = (
    (1, ("Farmer")),
    (2, ("Investor")),
    (3, ("Employee")),
)
class SignUpForm(UserCreationForm):
    first_name  = forms.CharField()
    last_name   = forms.CharField()
    # birth_date  = forms.DateField()
    #status      = forms.IntegerField(choices=STATUS_CHOICES)
    status      = forms.ChoiceField(choices=STATUS_CHOICES)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'status','password1', 'password2', )
