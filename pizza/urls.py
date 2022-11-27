from . import views
from django.urls import path
from django.urls import re_path as url
urlpatterns = [
    path('', views.home, name='home'),
    path('home.html', views.home, name='home'),
    path('order.html', views.order, name='order'),
]
