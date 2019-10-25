from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if 'title' in postData and len(postData['title']) < 5 :
            errors["title"] = "Blog name should be at least 5 characters"
        if 'network' in postData and len(postData['network']) < 5:
            errors["network"] = "Blog name should be at least 5 characters"
        if 'descr' in postData and len(postData['descr']) < 10:
            errors["descr"] = "Blog description should be at least 10 characters"
        if 'rday' in postData and len(postData["rday"]) > 0 and datetime.strptime(postData["rday"], '%Y-%m-%d') > datetime.today() :
            errors["rday"] = "Invalid release date."
        return errors


class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    rday = models.DateField()
    descr =models.CharField(max_length = 500)
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now = True)
    objects = BlogManager() 
