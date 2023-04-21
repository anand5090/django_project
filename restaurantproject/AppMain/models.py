from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class addBooks(models.Model):
    name=models.CharField(max_length=55)
    email=models.EmailField(max_length=55)
    number=models.IntegerField()
    date=models.DateField()
    person=models.IntegerField()