from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput
from django import  forms

from authenticate.models import HospitalProfile


class CreateHospitalForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
    )
    class Meta:
        model = User
        fields = ['username','first_name', 'email', 'password1', 'password2']
        widgets = {
            'username':TextInput(attrs={
                "required": 'true',
                "type": "text",
                "name": "username",
                "id": "username",
                "class":"form-control",
                "placeholder":"Create a unique Username for login purpose",
            }),
            'first_name':TextInput(attrs={
                "required": 'true',
                "type": "text",
                "name": "name",
                "id": "name",
                "class":"form-control",
                "placeholder":"Hospital Name",
            }),
            'email':EmailInput(attrs={
                "required":'true',
                "type": "email",
                "name": "email",
                "id": "email",
                "class":"form-control",
                "placeholder":'Email Id',
            })
        }

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
    )
    class Meta:
        model= User
        fields = ['username','email','first_name','last_name','password1','password2']
        widgets = {
            'username': TextInput(attrs={
                "required": 'true',
                "type": "text",
                "name": "username",
                "id": "username",
                "class": "form-control",
                "placeholder": "Create a unique username",
            }),
            'first_name': TextInput(attrs={
                "required": 'true',
                "type": "text",
                "name": "first-name",
                "id": "first-name",
                "class": "form-control",
                "placeholder": "Your first name",
            }),
            'last_name': TextInput(attrs={
                "required": 'true',
                "type": "text",
                "name": "last-name",
                "id": "last-name",
                "class": "form-control",
                "placeholder": "Your last name",
            }),
            'email': EmailInput(attrs={
                "required": 'true',
                "type": "email",
                "name": "email",
                "id": "email",
                "class": "form-control",
                "placeholder": 'Email Id',
            })
        }