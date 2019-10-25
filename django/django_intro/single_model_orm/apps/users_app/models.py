from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=46)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __repr__(self):
    return f"First Name: {self.first_name} ,\
        Last Name {self.last_name},\
            Email {self.email_address}"
