from django.urls import path
from .views import register, users

urlpatterns = [
    path('register/', register, name='register'),
    path('users/', users, name='users'),
]