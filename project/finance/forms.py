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
