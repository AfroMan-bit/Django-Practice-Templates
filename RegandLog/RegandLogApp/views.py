from django.shortcuts import render, redirect
from django.contrib import messages
# imported only after installing "bcrypt"
import bcrypt
from . models import *


# Create your views here.

# function to render "home.html"
def index(request):
    return render(request, "home.html")



# function to redirect the localhost:8000 to "home.html" 
def regpage(request):
    return redirect("/")


# function to handle the POST request for the route "register" from the registration form and after successful completion redirects to the "userprofile.html". unsuccesful registeration redirects back to the "home.html" with an error message.
def createReg(request):
    validationErrors = User.objects.registerValidator(request.POST)
    print(validationErrors)
    if len(validationErrors) > 0:
        for key, value in validationErrors.items():
            messages.error(request, value)
        return redirect("/")

    # encrypting the users password they submit by creating a variable "hashedpassword" to hold it. encrypting a string(password) the user registers with. also import bcrypt above after installing it with the "pip install bcrypt" in the command prompt.
    # variable = bcrypt module imported.built-in function called 'hashpw'(that accepts the string request.POST['key name'].and encrypt it 'encode()', creates random characters to scramble with the password to make it hard to read'bcrypt.gensalt().'
    hashedpassword = bcrypt.hashpw(request.POST['form_password'].encode(), bcrypt.gensalt()).decode()

    # variable = specify the fields in the ClassName
    newreguser = User.objects.create(first_name= request.POST['form_first_name'], last_name= request.POST['form_last_name'], email= request.POST['form_email'], password= hashedpassword)

    # add "session" to pass information for the particular user is logged in. Storing the userId in session makes it available to all the funtions
    # session variable[stored in a key] = the users Id in the database
    request.session['successfullyloggedinUserId'] = newreguser.id

    return redirect("/userprofile")


# function to handle the POST request for the route "login" form the Login form and after successful verification redirects to the "userprofile.html".Unsuccesful registeration redirects back to the "home.html" with an error message.
def userlogin(request):
    loginerrors = User.objects.loginValidator(request.POST)
    if len(loginerrors) > 0:
        for key, value in loginerrors.items():
            messages.error(request, value)
        return redirect ("/")
    else:
        # to get the user object from the list since the form is filled properly and the email and paswword match
        userlogin = User.objects.filter(email = request.POST['form_email'])
        userlogin = userlogin[0]
        # with the same session key 'successfullyloggedinUserId' from the registration form 
        request.session['successfullyloggedinUserId'] = userlogin.id
        # redirect to the "userprofile.html" from the route "login" for the Login form in the "home.html" which has a fuction of 'userlogin'
        return redirect("/userprofile")



# function that handles all successfull registration and successfull new users log in that renders "userprofile.html"
def logprofile(request):
    #  add "session" to pass information for which particular user is logged in. Storing the userId in session makes it available to all the funtions
    # variable = ClassName.get(id = session variable[stored in a key])
    loginuser = User.objects.get(id = request.session['successfullyloggedinUserId'])
    # add a dictionary
    context = {
        'successlogin': loginuser
    }
    return render(request, "userprofile.html", context)


def logout(request):
    # to clear the request.session "successfullyloggedinUserId"
    request.session.clear()
    return redirect("/")


