from django.forms import ModelForm
from django import forms
from nomadapp.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user']
