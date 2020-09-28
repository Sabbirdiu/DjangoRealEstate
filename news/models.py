from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username