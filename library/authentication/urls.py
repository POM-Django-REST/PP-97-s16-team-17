from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import register, users, CustomUserViewSet

router = DefaultRouter()
router.register(r'user', CustomUserViewSet, basename='user')

urlpatterns = [
    path('register/', register, name='register'),
    path('', users, name='users'),
]
