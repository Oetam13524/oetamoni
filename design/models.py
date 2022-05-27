from cgitb import text
from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    imageName = models.ImageField(upload_to="posts", null=True)
    bgimage = models.ImageField(upload_to="bgimages", null=True)
    description = models.TextField(max_length=1000, null=True)

    class Meta:
      verbose_name_plural = "posts"

    def __str__(self):
        return self.title