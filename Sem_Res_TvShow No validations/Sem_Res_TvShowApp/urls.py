from django.urls import path
from . import views

urlpatterns = [
    path("shows", views. index),
    path("shows/new", views. addnewshows),
    # form in the url "new" submits to a route "create" which is hidden from the user and handles POST request and assigning also a variable for each POST request.
    path("shows/create", views. createshows),
    # form in the url "new" redirects to the url "showInfo" with the variable "showId"
    path("shows/<showId>", views. showshows),
    path("shows/<showId>/edit", views. editshows),
    path("shows/<showId/update", views.updateshows),
    path("shows/<showId>/destroy", views.deleteshows),
]