from pyexpat import model
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core import serializers

from mvc import forms
from . import models
from mvc.models import Post
from mvc.forms import PostForm

# data = serializers.serialize("json", models.Post.objects.all())
# out = open('data.json', 'w')
# out.write(data)
# out.close()

# Create your views here.
def home(request):
    post = Post.objects.all()
    return render(request, 'post.html', locals())


def add_post(request):
    form = PostForm()
    if request.method == "POST":
        data = request.POST
        form = PostForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                pass
        else:
            form = PostForm()
    return render(request, 'index.html', {'form': form})
        
