from django.db import models

class GetUserInfo(models.Model):
     """ create user base for bot"""
     name = models.CharField(max_length=150)
     phone = models.CharField(max_length=150)

     def __str__(self):
          return self.name

class Services(models.Model):
     """ table with company advantages"""
     title = models.CharField(max_length=150)
     text = models.TextField()
     image = models.ImageField(upload_to='photos/')

     def __str__(self):
          return self.title

     class Meta:
          verbose_name = "Сервис"
          verbose_name_plural = 'Сервисы'

