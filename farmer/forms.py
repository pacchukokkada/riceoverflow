from dataclasses import field
from pyexpat import model
from django import forms
from .models import Farmer,Question,Answer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

# class UserCreationForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username','first_name','last_name','email','password1','password2')

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ("username","first_name","last_name" ,"email", "password1", "password2")
class FarmerCreationForm(forms.ModelForm):
    def phone_validation(phone_no):
        if len(phone_no) != 10:
            raise ValidationError("Invalid Phone Number!")
    phone = forms.CharField(max_length=10,validators=[phone_validation])
    class Meta:
        model = Farmer
        fields = ('phone','place','taluk','district','state','pincode','crops')
        widgets ={}

class FarmerUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ("username","first_name","last_name" ,"email")

        

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question','description')

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('answer',)

        
