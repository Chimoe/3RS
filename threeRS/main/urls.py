from django.contrib import admin
from django.urls import path, include
from signup.views import signup
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', signup, name='signup'),
    path('', include('reservation.urls')),
    path('admin/', admin.site.urls),
    url(r'^$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
