from django.db import models

# Create your models here.

class Post(models.Model):
    id =models.CharField(max_length=150, primary_key=True)
    text = models.CharField(max_length=200)
    likes = models.CharField(max_length=100)
    image_url = models.URLField(max_length = 200, default="")

    def __str__(self):
        return self.likes
