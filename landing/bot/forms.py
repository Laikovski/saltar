from django import forms
from .models import Settings_bot

class TgForm(forms.ModelForm):
    class Meta:
        model = Settings_bot()
        field = ['tg_token', 'tg_chat', 'tg_message']