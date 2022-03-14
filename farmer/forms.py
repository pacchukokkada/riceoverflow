from django import forms
from .models import Farmer,Question,Answer
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
class FarmerCreationForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ('phone','place','taluk','district','state','pincode','crops')
        
