from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    context = {
        "word": get_random_string(length=14),
        "attemptsTried": request.session['attempts'] ,
    }
    return render(request, "index.html", context)

def randomWord(request):
    if 'attempts' in request.session:
        request.session['attempts'] += 1
    return redirect("/")

def reset(request):
    request.session['attempts'] = 0
    return redirect("/")