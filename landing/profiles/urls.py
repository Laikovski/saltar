from django.urls import path
from .views import LoginPage, RegisterPage, UserCabinet, EditCabinet, LogoutUser

urlpatterns = [
    path('login/', LoginPage, name='login'),
    path('register/', RegisterPage, name='register'),
    path('cabinet/', UserCabinet, name='cabinet'),
    path('edit/', EditCabinet, name='edit'),
    # path('work/', EditCabinet, name='work'),
    path('logout/', LogoutUser, name='logout'),

]
