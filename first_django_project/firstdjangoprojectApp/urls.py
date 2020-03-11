from django.urls import path 
from . import views

urlpatterns = [
    # path("", views.home),
    path("", views.index),
    path("new", views.new),
    path("create", views.create),
    path("<integer>", views.show),
    path("<modify>/edit", views.edit),
    path("<remove>/delete", views.destroy),

]  