from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_list, name='author_list'),
    path('<int:author_id>/', views.author_detail, name='author_detail'),
    path('create/', views.author_create, name='author_create'),
    path('<int:author_id>/edit/', views.author_update, name='author_update'),
    path('<int:author_id>/delete/', views.author_delete, name='author_delete'),
]