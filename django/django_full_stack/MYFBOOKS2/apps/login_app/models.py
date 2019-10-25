from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
import re

# pip install validate_email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

# password rules
rulesp =[lambda s: any(x.isupper() for x in s), # must have at least one uppercase
        lambda s: any(x.islower() for x in s),  # must have at least one lowercase
        lambda s: any(x.isdigit() for x in s),  # must have at least one digit
        lambda s: len(s) >= 8  and len(s) <= 50,  # must be at least 7 characters
        ]
# first, last name rules    
rulesn =[lambda s: any(x.isalpha() for x in s), # must be letters      
        lambda s: len(s) > 2  and len(s) < 20,  # must be at least 2 characters
        ]

passstring = "password must have at least one uppercase \nat least one lowercase\n \
    at least one digit\nat least 7 characters and no more than 50 characters long."
    

class RegistrationManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if 'username' in postData and len(postData['username']) < 5 :
            errors["username"] = "username should be at least 5 characters"
        
        if not all(rule(postData['first_name']) for rule in rulesn):
            errors["first_name"] = "First Name should be at least 8 characters long and should include only letters."

        if not all(rule(postData['last_name']) for rule in rulesn):
            errors["last_name"] = "Last Name should be at least 8 characters long and should include only letters."
        
        if not EMAIL_REGEX.match(postData['email']): 
            errors["email"]  = "Invalid email format." 

        if not all(rule(postData['password']) for rule in rulesp):
            errors["password"] = passstring
        if  postData['password'] != postData['password2']:
            errors["password"] = "Password do not match"
            
        return errors


class MyUser(models.Model):
    username = models.CharField(max_length = 255)
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    password = models.CharField(max_length = 255)
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now = True)
    objects = RegistrationManager() 
