from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:building_id>/', views.detail, name='detail'),
    path('<int:building_id>/results/', views.results, name='results'),
    path('<int:building_id>/take/', views.take, name='take'),
    url(r'^logout/$', views.logoutView, name='logout'),
    url(r'^home/$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
]