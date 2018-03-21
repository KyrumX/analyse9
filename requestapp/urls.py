"""week1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from requestapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^week3/$', views.Week3Basic.as_view(), name='week3'),
    url(r'^week4/$', views.Week4.as_view(), name='week4overview'),
    url(r'^week4/create$', views.Week4Create.as_view(), name='week4create'),
]
