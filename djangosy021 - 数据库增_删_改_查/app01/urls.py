"""djangosy021 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from app01 import views


urlpatterns = [
    path('login/', views.login),
    path('orm/', views.orm),
    path('index/', views.index),
    path('userdetail-<str:nid>/', views.user_detail),
    path('user_info/', views.user_info),
path('userdel-<str:nid>/', views.user_del),
path('useredit-<str:nid>/', views.user_edit),



]
