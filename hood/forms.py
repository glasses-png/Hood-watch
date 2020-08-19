from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile
from .models import NeighbourHood,Business


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2'] 

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email'] 

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio']

class NeighbourHoodForm(forms.ModelForm):

    class Meta:
        model = NeighbourHood
        fields= ['name','location','description','hood_logo','police_number','health_tell']


class BusinessForm(forms.ModelForm):

    class Meta:
        model = Business
        fields = ['name','email']