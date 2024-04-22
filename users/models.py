from django.db import models
import  uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver
"""
post_save:trigger anytime the whe the post or save in the database aftrer 
"""

# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True) # any time when we delete the profile we delete the usere in the databease using model.CASCADE
    name=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(max_length=500,null=True,blank=True)
    username=models.CharField(max_length=255,null=True,blank=True)
    headline=models.CharField(max_length=500,null=True,blank=True)
    bio=models.TextField(blank=True,null=True)
    location=models.CharField(max_length=255,null=True,blank=True)
    profleImage=models.ImageField(
        blank=True,null=True,upload_to='profile/',default='profile/user.png')
    github=models.CharField(max_length=500,null=True,blank=True)
    linkedln=models.CharField(max_length=500,null=True,blank=True)
    presionalWebsite=models.CharField(max_length=500,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user.username)



class Skill(models.Model):
    owner=models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    descreption = models.TextField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

