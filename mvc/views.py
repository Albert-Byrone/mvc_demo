from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from . import models
from mvc.models import Post


# data = serializers.serialize("json", models.Post.objects.all())
# out = open('data.json', 'w')
# out.write(data)
# out.close()

# Create your views here.
def home(request):
    post = Post.objects.all()
    return render(request, 'post.html', locals())

