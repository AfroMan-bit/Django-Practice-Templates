from django.shortcuts import render, redirect
from . models import *

# Create your views here.

# FUNCTIONS FOR BOOK OBJECTS

# redirect url function below
def index(request):
    book = Book.objects.all()
    context = {
        'books': book,
    }
    return render(request, "index.html", context)

# 'books' url function below, redirected to index.html
def add_book(request):
    newbook = Book.objects.create( 
        title = request.POST['title'],
        desc = request.POST['desc'])
    print(newbook)
    return redirect("/")

# 'bookInfo' url function below, with the variables of 'bookId', as it renders on 'bookInfo.html'
def showbookInfo(request, bookId):
    showbook = Book.objects.get(id= bookId)
    context = {
        'book': showbook,
        'allauthors': Author.objects.all()
    }
    return render(request, "bookInfo.html", context)

# 'authorTobook' url function below, with the variables of 'authorId', as it redirects to 'bookInfo.html'
def authorTobook(request, authorId):
    author = Author.objects.get(id = authorId)
    author = Author.objects.get(id = request.POST['authorid'])
    author.authors.add(author)
    return redirect(f"bookInfo/{authorId}")




# FUNCTIONS FOR AUTHOR OBJECTS

# 'author' url function below, redirected to itself('author.html') from a link on the index.html page as a GET request and then redirects to itself('author.html') as a POST request
def add_author(request):
    if request.method == "GET":
        author = Author.objects.all()
        context = {
            'authors': author,
    }
        return render(request, "author.html", context)
    if request.method == "POST":
        newauthor = Author.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            notes = request.POST['notes'])
        print(newauthor)
        return redirect("author.html")


# 'authorInfo' url below with the variables of 'authorId', as it renders on 'authorInfo.html'
def showauthorInfo(request, authorId):
    context = {
        'author': Author.objects.get(id=authorId),
        'allbooks': Book.objects.all()
    }
    return render(request, "authorInfo.html", context)


# 'bookToauthor' url function below, with the variables of 'bookId', as it redirects to 'authorInfo.html'
def bookToauthor(request, bookId):
    book = Author.objects.get(id = bookId)
    book = Author.objects.get(id = request.POST['bookid'])
    book.books.add(book)
    return redirect(f"authorInfo/{bookId}")