from django import forms


class PersonCreateForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    full_name = forms.CharField(required=True)
    birthday =  forms.DateField(required=True)
    gender  =  forms.CharField(required=True)
    profile_picture = forms.ImageField(required=False)
    NID =forms.CharField(required=True)
    email =forms.EmailField(required=True)
    qualification = forms.CharField(required=True)
    mobile_no = forms.CharField(required=True)
    address = forms.CharField(required=True)
    bank_credentials=forms.CharField(required=True)
    title = forms.CharField(required=True)
