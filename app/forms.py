from django import forms
from django.forms import ModelForm

from .models import *


class add_todoForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Add new task....'}))

    description = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': "Add task's description..", 'class': 'your_css_code'}))

    class Meta:
        model = add_todo
        fields = '__all__'
