from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name = 'home'),
    url(r'^logout/$', views.logoutView, name='logout'),
]