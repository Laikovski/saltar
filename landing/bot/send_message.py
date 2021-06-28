import requests
from .models import Settings_bot


def send_message(name, phone):
    """Create request and send message to Telegram"""
    settings = Settings_bot.objects.get(pk=1)
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat)
    text = str(settings.tg_message)

    part_1 = text[:text.find('{')]
    part_2 = text[text.find('}')+1:text.rfind('{')]

    message = f'{part_1} {name}{part_2}{phone}'
    api = 'https://api.telegram.org/'
    method = f'{api}{token}/sendMessage'
    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': message
    })

