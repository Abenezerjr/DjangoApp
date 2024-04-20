from django.db import models
import  uuid
# Create your models here.


class Profil(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    username=models.CharField(max_length=255,null=True,blank=True)
    headline=models.CharField(max_length=500,null=True,blank=True)
    bio=models.TextField(blank=True,null=True)
    location=models.CharField(max_length=255,null=True,blank=True)
    profleImage=models.ImageField(upload_to='profile/',default='default.jpg')
    github=models.CharField(max_length=500,null=True,blank=True)
    linkedln=models.CharField(max_length=500,null=True,blank=True)
    presionalWebsite=models.CharField(max_length=500,null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created=models.DateTimeField


