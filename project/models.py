from django.db import models
import uuid
# Create your models here.


class Project(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(null=True,blank=True)
    demoLink=models.CharField(max_length=2000,blank=True,null=True)
    sourceLink=models.CharField(max_length=2000,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False)


    def __str__(self):
        return  self.title