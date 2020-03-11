from django.db import models

# Create your models here.
class Movie(models.Model):
    # id ----->   is automatically added but hidden
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# type in the terminal after running the shell---->  from First_ORM_App.models import Movie ('Movie' in this case is the class mentioned in this First_ORM_App.model file)
    # OR
# type in the terminal after running the shell---->  from First_ORM_App.models import * (not encouraged but it can also be used if we want to get data from all the contents in the First_ORM_App.model file)

# to change how models display we use this method below
    # def __repr__(self):
    #     return "Title: {}".format(self.title)
    # OR
    # def __repr__(self):
    #     return f"<Movie object: {self.title} ({self.id})>" 
        # ('Movie' in this case is the class mentioned in this First_ORM_App.model file)
    # OR
    # installing iPython -----> pip install ipython

