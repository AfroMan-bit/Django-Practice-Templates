from django.db import models
# this module below allows to manipulate strings in certain ways
import re
# this import bcrypt here also
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    # function to validate the registration form's POST request. "self" means to validate with the requirements
    def registerValidator(self, postData):
        errors = {}
        # pathern validation which is stored in the variable "EMAIL_REGEX" uses "re.compile" and takes a (raw)"r"string and accepts only a certain format like [a-zA-Z0-9.+_-]which means ( e.g any characters btw a-z, A-Z, 0-9, ."decimal", +"plus", _"underscore", -"dash") +@ (and an "@" symbol then) [a-zA-Z0-9.+_-] +\. (and a "." dot symbol) then [a-zA-Z]+$ (the "$" is to signify the end of the string
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # adding a filter in the database to ensure no information about a new user registering is repeated again in the already exiting database.
        # variable = ClassName.objects.filter(field1= value['key name'])
        usersWithEmail = User.objects.filter(email= postData['form_email'])

        if len(postData['form_first_name']) < 1:
            errors['FirstNameRequired'] = "First name is required"
        if len(postData['form_first_name']) < 1:
            errors['LastNameRequired'] = "Last name is required also"
        if len(postData['form_email']) < 2:
            errors['EmailRequired'] = "A proper email format is required"
        # this is to verify if the email format is correct
        elif not EMAIL_REGEX.match(postData['form_email']):
            errors['EmailFormat'] = "Email is not in a valid format"
        # this is to verify if a new users email already exist in the database
        elif len(usersWithEmail) > 0:
            errors['DifferentEmailRequired'] = "Email already exist"
        if len(postData['form_password']) < 3:
            errors['PasswordRequired'] = "This holds the key to your account and must be atleast 3 characters so obviously...."

        # for "password" and "confirm_password" to be compared, by stating that if they are not equal or the same the error should be given to the user.
        if postData['form_password'] != postData['form_confirm_password']:
            errors['ConfirmPasswordRequired'] = "The key to your account do not match please try again"
        return errors


    # function to validate the user login form's POST request. "request" means to compare information with the database.
    def loginValidator(request, postData):
        errors = {}
        # to see if the login email is existing in the database for access to successfull login
        # adding a filter in the database to ensure only information about an existing user loging in gains access to the userprofile.html.
        # variable = ClassName.objects.filter(field1= value['key name'])
        usersWithEmail = User.objects.filter(email= postData['form_email'])
        # if there are no emails that exit in the database when logging in give the user an error message
        if len(usersWithEmail) == 0:
            errors['EmailmatchRequired'] = "Profile does not exist, Please register first"
        # if the email exits in the database, also check the password if it exist also
        else:
            # this gives access to the password in the form and can be compared
            user = usersWithEmail[0]
            # check the bcrypt password of the user trying to login if it is the same with what is stored for them in our database.
            # if the bcrypt function "ckeckpw" which is an in-built function for bcrypt to check passwords (we check the POST request which is in the variable "postData" from the form for login['key name'].encode(), name of object which is "user".ClassName field assigned for password which is "password".encode()):
            # format explained -->if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
     
            if bcrypt.checkpw(postData['form_password'].encode(), user.password.encode()):
                print("password match")
            else:
                errors['PasswordMatch'] = "Password is Invalid"
        return errors




class User(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

