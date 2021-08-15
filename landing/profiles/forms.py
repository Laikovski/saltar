from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# class LoginUserForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(LoginUserForm, self).__init__(*args, **kwargs)
#
#     username = forms.EmailField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': '',
#             'id': 'hi',
#         }
#     ))



class LoginForm(forms.ModelForm):
    '''Simple login form'''
    class Meta:
        model = User
        fields = ('username', 'password')