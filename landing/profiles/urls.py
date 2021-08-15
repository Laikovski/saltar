from django.urls import path
from .views import LoginForms

urlpatterns = [
    path('login/', LoginForms.as_view(), name='login'),

]
