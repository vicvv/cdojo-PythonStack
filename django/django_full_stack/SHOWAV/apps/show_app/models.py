from django.db import models

class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    rday = models.DateField()
    descr =models.CharField(max_length = 500)
    created_at = models.DateField(auto_now = True)
    updated_at = models.DateField(auto_now = True)
