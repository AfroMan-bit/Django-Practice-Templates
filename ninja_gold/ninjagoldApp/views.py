from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if 'total' not in request.session:
        request.session['total']= 0
    if 'activity' not in request.session:
        request.session['activities']= []
    return render(request, "index.html")

def process(request):
    print(request.POST)
    currentTime = datetime.now()
    if request.POST['location'] == "farm":
        goldEarned = random.randint(10,20)
        request.session['total'] += goldEarned
        activity = f"Went to farm and earned {goldEarned} - {currentTime}"
        request.session['activities'].append(activity)
    if request.POST['location'] == "cave":
        goldEarned = random.randint(5,10)
        request.session['total'] += goldEarned
        activity = f"Went to cave and earned {goldEarned} - {currentTime}"
        request.session['activities'].append(activity)
    if request.POST['location'] == "house":
        goldEarned = random.randint(2,5)
        request.session['total'] += goldEarned
        activity = f"Went to house and earned {goldEarned} - {currentTime}"
        request.session['activities'].append(activity)
    if request.POST['location'] == "casino":
        goldEarned = random.randint(-50,50)
        request.session['total'] += goldEarned
        if goldEarned < 0:
            goldEarned = abs(goldEarned)
            activity = f"Went to casino and lost {goldEarned} - {currentTime}"
            request.session['activities'].append(activity)
        else:
            activity = f"Went to casino and earned {goldEarned} - {currentTime}"
            request.session['activities'].append(activity)
            
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")

