from django import forms
from .models import Customer

class SignUp(forms.Form):
    fName = forms.CharField(max_length=25, label='', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lName = forms.CharField(max_length=25, label='', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    phoneNumber = forms.CharField(max_length=10, label='', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    street_number = forms.CharField(max_length = 20, label='', widget=forms.TextInput(attrs={'placeholder': 'Street Number'}))
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={'type': 'email',
               'placeholder': 'E-mail address'}))
