from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.add_book),
    path('bookInfo/<bookId>', views.showbookInfo),
    path('authorTobook/<authorId>', views.authorTobook),
    path('author', views.add_author),
    path('authorInfo/<authorId>', views.showauthorInfo),
    path('bookToauthor/<bookId>', views.bookToauthor),
]