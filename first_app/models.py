from django.db import models

# Create your models here.

class Message(models.Model):
    
    sender=models.CharField(max_length=256)
    receiver=models.CharField(max_length=256)
    message=models.CharField(max_length=1248)
    subject=models.CharField(max_length=312)
    creation_date=models.DateField()
    read=models.BooleanField(default=False)

