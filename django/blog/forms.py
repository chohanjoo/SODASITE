from django import forms
from .models import Project
from django.forms import ModelForm, Textarea
from django_summernote.widgets import SummernoteWidget



class PostForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','content','project_file']
        widgets = {
            'content': SummernoteWidget(),
           
        }

   