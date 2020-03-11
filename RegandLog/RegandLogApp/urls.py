from django.urls import path
from . import views

urlpatterns = [
    path('', views. index),
    path('home', views. regpage),
    path('register', views. createReg),
    path('login', views. userlogin),
    path('userprofile', views. logprofile),
    path('logout', views. logout),
    
]