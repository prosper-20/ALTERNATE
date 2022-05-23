from django.contrib import admin
from .models import Category, Services, Message, Work, Consultation, Gallery, Staff

# Register your models here.


admin.site.register(Category)
admin.site.register(Services)
admin.site.register(Work)
admin.site.register(Gallery)



class MessageAmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']



admin.site.register(Message, MessageAmin)

class ConsultationAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "company_name"]


admin.site.register(Consultation, ConsultationAdmin)


class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'job']


admin.site.register(Staff, StaffAdmin)