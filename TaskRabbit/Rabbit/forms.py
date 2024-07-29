from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class ImageForm(forms.ModelForm):
    class Meta:
        model=UserImage
        fields='__all__'