from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('randomWord', views.randomWord),
    path('reset', views.reset),

    
]