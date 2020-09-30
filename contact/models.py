from django.db import models
from ckeditor.fields import  RichTextField
from datetime import datetime


# Create your models here.
class About(models.Model):
    description = RichTextField(blank=True,null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
class Partnars(models.Model):
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/')
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100,blank=True)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name