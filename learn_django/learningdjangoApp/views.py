from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

def showsignupPage(request):
    return HttpResponse("here is a page for signing up")

def showspremiumMembers(request):
    return render(request, "premiumSignup.html")

def showinteger_only(request, itemId):
    return HttpResponse(f"showing item number {itemId}")

def showitem_integer_or_words(request, itemId):
    return HttpResponse(f"showing item for integer or words {itemId}")

def logout(request):
    return redirect("/")
    