from django.contrib import admin
from .models import  Category, Post, Consultation
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "date_posted"]

admin.site.register(Post, PostAdmin)
admin.site.register(Category)

class ConsultationAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "company_name"]


    
