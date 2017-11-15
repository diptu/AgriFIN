from django import forms

from .models import Farmer
# from .validators import validate_category

class FarmerCreateForm(forms.ModelForm):
    #email           = forms.EmailField()
    #category         = forms.CharField(required=False, validators=[validate_category])
    class Meta:
        model = Farmer
        fields = [
            'username',
            'full_name',
            'age',
            'gender',
            'address',
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name
