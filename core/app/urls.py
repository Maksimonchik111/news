from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.post_list, name='index'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail')
]
