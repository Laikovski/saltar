from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Work
from django.forms import TextInput, EmailInput, DateInput


class LoginForm(forms.ModelForm):
    '''Simple login form'''
    class Meta:
        model = User
        fields = ('username', 'password')


class CreateUserForm(UserCreationForm):
    '''Register User Form'''
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'auth-field', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'class': 'auth-field', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'username': TextInput(attrs={'class': 'auth-field', 'placeholder': 'Введите логин'}),
            'email': EmailInput(attrs={'class': 'auth-field', 'placeholder': 'Введите email'}),
        }

class UpdateProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('name', 'phone', 'car_model', 'car_number', 'vin')

    widgets = {
        'name': TextInput(attrs={'class': 'auth-field', 'placeholder': 'Введите имя'}),
    }

class AddWork(forms.ModelForm):

    class Meta:
        model = Work
        fields = ('work_name', 'date')

    widgets = {
        'work_name': TextInput(attrs={'class': 'auth-field', 'placeholder': 'Введите наименование работы'}),
        'date': DateInput(attrs={'class': 'auth-field'}),
    }