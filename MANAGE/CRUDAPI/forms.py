from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Medicine
from django import forms
from django.db import models



from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# - Register/Create a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create a record

class Create(forms.ModelForm):

    class Meta:

        model = Medicine
        fields = ['m_id', 'mname', 'desc', 'price', 'stock']


# # - Update a record

class Update(forms.ModelForm):

    class Meta:

        model = Medicine
        fields = ['mname', 'desc', 'price', 'stock']



class Search(forms.Form):
    query = forms.CharField(label='search', max_length=100)

