from django.urls import path
from . import views

app_name = 'reserve'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:building_id>/', views.detail, name='detail'),
    path('<int:building_id>/results/', views.results, name='results'),
    path('<int:building_id>/take/', views.take, name='take'),

]