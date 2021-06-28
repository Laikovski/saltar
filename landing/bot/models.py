from django.db import models

# Create your models here.
class Settings_bot(models.Model):
    tg_token = models.CharField(max_length=150, verbose_name='Токен')
    tg_chat = models.CharField(max_length=150, verbose_name='ID')
    tg_message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.tg_chat

class Meta:
    verbose_name = "Настройка"
    verbose_name_plural = 'Настройки'