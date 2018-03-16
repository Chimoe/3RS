from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    url(r'', include('reserve.urls')),
    url(r'^$', auth_views.LoginView.as_view(template_name='reserve/login.html'), name='login'),
]