from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import  RichTextField

class Realtor(models.Model):
  name = models.CharField(max_length=200)
  slug = models.SlugField()
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
        return reverse('agent-details', kwargs={
            'slug': self.slug
        })  

SERVICE_TYPE = (
  ('For Rent','For Rent'),
  ('For Sale','For Sale'),
)
RENT_TYPE = (
  ('M','M'),
  ('Y','Y'),
)

class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  slug = models.SlugField()
  location = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = RichTextField(blank=True)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  kitchen = models.IntegerField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  video  = models.FileField(upload_to="video/%y",null=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  featured = models.BooleanField()
  servicetype = models.CharField(choices = SERVICE_TYPE,max_length=30,null=True)
  rent = models.CharField(choices = RENT_TYPE,max_length=30,null=True)   
  def __str__(self):
    return self.title
  def get_absolute_url(self):
        return reverse('listing', kwargs={
            'slug': self.slug
        })  