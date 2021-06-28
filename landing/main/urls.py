from django.contrib import admin
from django.urls import path, include
from .views import open_main_page

urlpatterns = [

    path('', open_main_page, name='index_page'),

]