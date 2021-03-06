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

    path('cmdb/',include("app01.urls")),
    path('monitor/', include("app02.urls")),

]

""" path('admin/', admin.site.urls),
   path('indexgkutgkg/<nid>', views.index,name = "indexx"),
   path('login/', views.login),
   #path('home/', views.home),
   path('home/', views.Home.as_view()),
   #path('detail/', views.detail),
   path('detail-<str:nid>.html', views.detail),"""
