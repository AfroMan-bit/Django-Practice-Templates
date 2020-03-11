from django.db import models

# Create your models here.



# for back-end validation create a "class ClassNameManager(models.Manager)" model in our models.py file.
class ShowManager(models.Manager):
    # add a function (e.g showValidator or any custom name) and also add a parameter (variable) to hold the request.POST from the form (e.g "postData" or any custome name)
    def showValidator(self, postData):
        # create a dictionary (e.g "errors" or any custom name) 
        errors = {}
        # if the information from the user filling the form does not meet the requirement then back-end validation sends the error message. (e.g"title" cannot be less than 2 characters if not this funtion will post the error message)
        if len(postData['form_title']) < 2:
            errors['TitleRequired'] = "Title name is required, it cannot be empty"

        # this means if request.POST(variable) which is the information passed from the form[name given to the "name" attitbute in the input tag in the form] doesnt meet the requirement condition
        if len(postData['form_network']) < 3:
            # this is a key (e.g "NetworkRequired") that has a value (message) attached to it 
            errors['NetworkRequired'] = "Please fill out the Network name"

        # ths below is not correct for setting the requirement for date.
        # if len(postData['form_release_date']) < 0:
        #     errors['ReleasedateRequired'] = "Release date is important, Release date cannot be empty"

        if len(postData['form_desc']) < 5:
            errors['DescriptionRequired'] = "Sigh...please fill out the form correctly"
        # if it meets the requirements (< 5 characters) given for the "name" attribute but still doesnt meet the minimum requrement which is (< 10 characters) we can send another error message
        elif len(postData['form_desc']) < 10:
            errors['DescriptionNotLongEnough'] = "Description is too short, must be 10 characters long"
        # if it doesnt meet the requirement give the error message
        return errors




# Models for the database data starts below

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=225)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# for back-end validation, refering to a class (e.g ShowManger), then we create a class ShowManager(models.Model) above in our models.py file. DONT FORGET TO MIGRATE AGAIN AFTER ADDING BACK-END VALIDATIONS
    objects = ShowManager()


