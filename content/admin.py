from django.contrib import admin
from .models import Category, Services, Message

# Register your models here.


admin.site.register(Category)
admin.site.register(Services)



class MessageAmin(admin.ModelAdmin):
    list_display = ['name', 'email']



admin.site.register(Message, MessageAmin)