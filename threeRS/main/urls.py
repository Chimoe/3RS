from django.contrib import admin
from django.urls import path, include
from signup.views import signup

urlpatterns = [
    path('', signup, name='signup'),
    path('buildings/', include('reservation.urls')),
    path('admin/', admin.site.urls),
]
