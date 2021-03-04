from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'image', 'streetNum', 'city', 'state', 'zipcode')

class SignUp(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='')
    last_name = forms.CharField(max_length=30, required=True, help_text='Optional.')
    phoneNumber = forms.CharField(max_length=10, help_text='', required=True,
                                  widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    street_number = forms.CharField(max_length=20, help_text='', required=True,
                                    widget=forms.TextInput(attrs={'placeholder': 'Street Number'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)