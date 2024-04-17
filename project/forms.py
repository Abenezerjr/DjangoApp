from  django.forms import ModelForm
from . models import Project



class AddProjectForm(ModelForm):
    class Meta:
        model=Project
        fields=['title','description','demoLink','sourceLink','tags','feature_image']