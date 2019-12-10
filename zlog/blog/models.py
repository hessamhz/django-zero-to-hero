from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your models here.


class BlogPost(models.Model):

    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=240)
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    CHOICES = (('K', 'Kids'), ('M', 'Mature'), ('E', 'Everyone'))
    target_age = models.CharField(max_length=1, choices=CHOICES)

# pip install virtualenv
# venv envname/
# source envname/bin/activate
# deactive
# pip install django
# django-admin startprojet zlog
# cd zlog
# django-admin startapp blog
