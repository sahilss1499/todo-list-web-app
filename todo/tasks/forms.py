from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(forms.ModelForm):
    #to add widgets to form created from ModelForm
    class Meta():
        model = Task
        fields = '__all__'
        #to add widgets to form created from ModelForm
