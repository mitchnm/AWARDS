from .models import Project, Profile
from django import forms
from django.forms import ModelForm, Textarea, IntegerField


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['name']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'comments', 'user', 'profile']
