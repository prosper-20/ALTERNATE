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
        verbose_name_plural = "Services"


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
    link = models.URLField()

    def __str__(self):
        return(self.category.name)


class Consultation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=300)
    website = models.URLField(blank=True, null=True)
    message = models.TextField(help_text="How can we help of service to you?")

    def __str__(self):
        return(f"{self.first_name} - {self.email} - {self.company_name}")


class Gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery_pics")

    def __str__(self):
        return self.name


