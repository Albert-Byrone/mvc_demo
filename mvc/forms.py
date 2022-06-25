from dataclasses import field
from pyexpat import model
from django import forms

from mvc.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"