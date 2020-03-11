from django.urls import path
from . import views

urlpatterns = [
    path("shows", views. index),
    path("shows/new", views. addnewshows),
    # form in the url "new" submits to a route "create" which is hidden from the user and handles POST request 
    # and back-end validation and also assigning a variable for each POST request that is finally redirected to "showInfo.html"
    path("shows/create", views. createshows),
    # form in the url "new" redirects to the url "showInfo" with the variable "showId"
    path("shows/<showId>", views. showshows),
    path("shows/<showId>/edit", views. editshows),
    # form in the url "shows/{{showing.id}}/edit" submits to a route "update" which is hidden from the user 
    # in the "edit.html" file and handles POST request and back-end validation
    # and also assigning a variable for each POST request theat is finally redirected to "showsInfo.html".
    path("shows/<showId/update", views.updateshows),
    path("shows/<showId>/destroy", views.deleteshows),
]