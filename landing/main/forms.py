from django import forms
from .models import GetUserInfo

class UpperForm(forms.ModelForm):
    class Meta:
        model = GetUserInfo
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'size': 30, 'class': 'set-input'}),
            'phone': forms.TextInput(attrs={'size': 30, 'class': 'set-input'}),

        }

