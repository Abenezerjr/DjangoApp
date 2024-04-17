from  django.forms import ModelForm
from django import forms
from . models import Project



class AddProjectForm(ModelForm):
    class Meta:
        model=Project
        fields=['title','description','demoLink','sourceLink','tags','feature_image']

        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(AddProjectForm,self).__init__(*args,**kwargs)
        #
        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add project title'})
        # self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'Add project description'})


        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
            self.fields['feature_image'].widget.attrs.update({'class': 'btn btn--sub'})