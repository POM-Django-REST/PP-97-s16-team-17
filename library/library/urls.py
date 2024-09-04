from django.contrib import admin
from django.urls import path, include

from book.serializers import BookSerializer
from . import views
from rest_framework.routers import DefaultRouter
from authentication.views import CustomUserViewSet
from rest_framework_nested import routers
from order.views import OrderViewSet
from book.views import BookViewSet
from author.views import AuthorViewSet

router = routers.DefaultRouter()
router.register(r'user', CustomUserViewSet, basename='user')
router.register(r'order', OrderViewSet, basename='order')
user_router = routers.NestedDefaultRouter(router, r'user', lookup='user')
user_router.register(r'order', OrderViewSet, basename='user-order')
router.register(r'book', BookViewSet, basename='book')
router.register(r'author', AuthorViewSet, basename='author')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login_user/', views.login_view, name='login_user'),
    path('logout/', views.logout_view, name='logout'),
    path('authors/', include('author.urls')),
    path('users/', include('authentication.urls')),
    path('books/', include('book.urls')),
    path('orders/', include('order.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(user_router.urls)),
]
