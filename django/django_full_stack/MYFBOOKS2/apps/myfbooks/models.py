from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
from .. login_app.models import *



class BookManager(models.Manager):
    def input_validator(self, postData):
        errors = {}
        if 'title' not in postData  or len(postData['title']) < 2:
                errors['title'] = "Please provide a valid Book Title!"
        if 'description' not in postData or len(postData['description']) < 5:
            errors["description"] = "Please add Book Description!"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=600)
    uploaded_by = models.ForeignKey(MyUser, related_name="books_uploded",on_delete=models.CASCADE)
    likes = models.ManyToManyField(MyUser, related_name="liked_books")
    objects = BookManager()
