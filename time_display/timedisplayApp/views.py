from django.shortcuts import render, HttpResponse, redirect
# from time import gmtime, strftime
# OR
from datetime import datetime

def index(request):
    context = {
        # "time": strftime("%b, %m-%d %H:%M %p", gmtime())

        # OR
 
        "time": (datetime.now)
        # "number": list(range(10))
    } 
 
    return render(request, "index.html", context)

def homepage(request):
    context = {
        # "htmlname": name,
        "namelist": ["Ana", "Ben", "Jacob",]
    }
    return render(request, "home.html", context)
#     # return HttpResponse(f"Hello this is the Home Page {name}")

def process(request):
    print(request.POST)
    request.session["name"]= request.POST["name"]
    return redirect("/home")

# # Create your views here.


