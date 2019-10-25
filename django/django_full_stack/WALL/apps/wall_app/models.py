from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
from .. login_app.models import MyUser


class Message(models.Model):
    messagetext = models.CharField(max_length=600)
    created_by = models.ForeignKey(MyUser, related_name="message_created",on_delete=models.CASCADE)   
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now = True)

class Coment(models.Model):
    commenttext = models.CharField(max_length=600)
    creator = models.ForeignKey(MyUser, related_name="comment_created",on_delete=models.CASCADE)
    tomessage =  models.ForeignKey(Message, related_name="comment_to_message",on_delete=models.CASCADE)  
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now = True)

