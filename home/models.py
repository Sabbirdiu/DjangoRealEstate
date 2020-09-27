from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse

class Realtor(models.Model):
  name = models.CharField(max_length=200)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  description = models.TextField(blank=True)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  ownaddress = models.CharField(max_length=50)
  agency = models.CharField(max_length=50)
  company= models.CharField(max_length=50)
  licenses= models.CharField(max_length=50)
  number=models.CharField(max_length=50)
  agencyaddress=models.CharField(max_length=50)
  hire_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.name
  def get_absolute_url(self):
        return reverse('agent-details',kwargs={'pk':self.pk})  