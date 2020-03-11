from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


# def home(request):
#     return HttpResponse("placeholder to display the list of all blogs")

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] += 1
    context= {
        "myarray": ["cat", "dog", "monkey", "moredog"],
        "somevalue": 52,
        "timesVisited": request.session['count'],
    }
    return render(request, "index.html", context)


def new(request): 
    return HttpResponse("placeholder to create a new form to crete a new blog")

def create(request):
    return redirect("/")

def show(request, integer):
    return HttpResponse(f"placeholder to display blog number {integer}")

def edit(request, modify):
    return HttpResponse(f"placeholder to edit blog number {modify}")

def destroy(request, remove):
    return redirect("/")