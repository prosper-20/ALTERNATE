from django.contrib import admin
from .models import Category, Services, Message, Work

# Register your models here.


admin.site.register(Category)
admin.site.register(Services)
admin.site.register(Work)



class MessageAmin(admin.ModelAdmin):
    list_display = ['name', 'email']



admin.site.register(Message, MessageAmin)