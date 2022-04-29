from distutils.command.upload import upload
from tabnanny import verbose
from time import time
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post_images")
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.title} - {self.author}"

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'slug': self.slug})




