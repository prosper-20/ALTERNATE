from email import message
from operator import mod
from tabnanny import verbose
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='service_images')
    content = models.TextField()

    class Meta:
        verbose_name_plural = "Service"


    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(help_text="Enter your email address")
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"


class Work(models.Model):
    image = models.ImageField(upload_to='work_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category