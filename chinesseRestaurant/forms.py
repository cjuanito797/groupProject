from django import forms
from .models import Customer

class SignUp(forms.Form):
    fName = forms.CharField(max_length=25, label='First Name')
    lName = forms.CharField(max_length=25, label='Last Name')
    phoneNumber = forms.CharField(max_length=10, label='Phone Number')
    address = forms.CharField(max_length=100)
    email = forms.EmailField()
