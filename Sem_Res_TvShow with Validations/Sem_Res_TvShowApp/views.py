from django.shortcuts import render, redirect
# this belowlinks the back-end messages from the model.py file to this views.py page
from django.contrib import messages
from . models import *

# Create your views here.


# the function "index" renders the localhost:8000 as a render request from "shows.html"
def index(request):
    # (to get all the objects to be viewed by the user in the url "shows" which is redirected to the "shows.html" with the function "index")
    # the variable "showallshows" represents a list of objects from the ClassName that can be passed to the url by using a dictionary which is redirected to the "shows.html" file. 
    # variable = ClassName.objects.all()
    showallshows = Show.objects.all()
    # the name of the dictionary below is called "context" with key value pairs ('dict_key': variable for the ClassName) i.e 'showingshows': showallshows
    context = {
        'showingshows': showallshows
    }
    # then add the dictionary name (context) inside the return render request
    return render(request, "shows.html", context)


# url "new" for the function "addnewshows"
def addnewshows(request):
    return render(request, "new.html")



# form in the url "new" submits to a url called "create" that does not display any template to the user 
# at all but only handles the POST request carrying all the data in the form from the url "new" which is 
# stored in a dictionary to redirect to the url "showInfo"
# (variable) is any "choice name" given to hold the the POST request, 'create' returns the object from 
# the database it creates and it is stored in the variable (newshow), 'field1' is in the ClassName of the models.py file)
def createshows(request):
# THIS BELOW HANDLES THE BACK-END REQUIREMENT FOR THE FORM 

    # From the function that holds the form url we can use back-end validation.  Back-end validation uses the "request.POST" 
    # in reference to the input tag "name" attribute given to it from the form to be submited as POST request
    #  (e.g <input type= "text" name="form_title" id="" class="form-control" required>). 
    # The name attribute is "form_title" that we use for the back-end validation and we add "required" for the front-end validation. 

    # variable from the models.py = ClassName.objects.function name given to the variable name "error" from the class Manager in models.py(request.POST) 
    errors = Show.objects.showValidator(request.POST)
    # if the error dictionary is greater than 0, it will go to the for loop and go through all the keys(key) and values(val) in the dictionary(error) and put all the values(val) in the "messages.error"("messages" allows you to display error to the user per one refresh and also must be available in the form html)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        # if there are errors it redirects to the form url "new.html" from the route "create"
        return redirect("/shows/new")

# THIS BELOW HANDLES THE POST REQUEST FOR THE FORM 

    # variable = ClassName.objects.create(field1=request.POST['name'], field2=request.POST['name'], field3=request.POST['name'])
    newshow = Show.objects.create(title= request.POST['form_title'], network= request.POST['form_network'], release_date= request.POST['form_release_date'], desc= request.POST['form_desc'])
    # then print the variable 'newshow' that stores the object
    print(newshow)
    # then use an 'f' string to redirect to the id of the object which is 'newshow.id'
    return redirect(f"showInfo/{newshow.id}")



# the url "<showId>" as a variable  for the function "showshows", which renders the POST request on "showInfo.html"
def showshows(request, showId):
    # variable to call out the ClassName = ClassName.objects.get(id=variable for specific ClassName fields)
    show = Show.objects.get(id = showId)
    # create a dictionary "context" with a 'dictionary name' which is "showing" and a dictionary key which is "show", the dictionary key is the same variable used to call out the ClassName
    context = {
        'showing': show
    }
    return render(request, "showInfo.html", context)



# the function "editshows" returns a template for the url "shows/showId/edit", WE CANT ADD VALIDATION HERE BECAUSE url "shows/showId/edit" just renders a template.
def editshows(request, showId):
    show = Show.objects.get(id = showId)
    context = {
        'show': show
    }
    return render(request, "edit.html", context)

# the function "updateshows" updates and then redirects to the "showS/showInfo.html", WE ADD THE VALIDATION HERE BECAUSE THE route "update" handles the POST request and REDIRECTS TO THE url "/shows/showInfo" to enforce the changes in "edit.html"
def updateshows(request, showId):
    # From the function that holds the form url we can use back-end validation. Back-end validation uses the "request.POST" in reference to the input tag "name" attribute given to it from the form to be submited as POST request (e.g <input type= "text" name="form_title" id="" class="form-control" required>). The name attribute is "form_title" that we use for the back-end validation and we add "required" for the front-end validation.

    errors = Show.objects.showValidator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        # if there are errors it redirects back to the form url "shows/{{showing.id}}/edit" from the route "update"
        return redirect(f"/shows/{showId}/edit")
        # OR 
        # return redirect("/shows/{{showing.id}}/edit")
    else:

        # variable = ClassName.objects.get(id= variable) then
	    # variable.field_name = request.POST['name'] then
	    # variable.save()
        # the variable name "update" is the ClassName object to be updated
        update = Show.objects.get(id = showId)
        update.title = request.POST['form_title']
        update.network = request.POST['form_network']
        update.release_date = request.POST['form_release_date']
        update.desc = request.POST['form_desc']
        update.save()

        # this below shows a message if the user fulfils all the requirements for filling out the form in the "edit.html" file 
        messages.success(request, "Successfully updated show")
        return redirect(f"/shows/{showId}")
        # OR 
        # return redirect("/shows/{{ show.id }}")

# the function "deleteshows" deletes and then redirects to the "show.html"
def deleteshows(request, showId):
    # variable = Show.objects.get(id= variable)
    # variable.delete()
    deleteshow = Show.object.get(id = showId)
    deleteshow.delete()
    return redirect("/shows")

   


