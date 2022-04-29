# from attr import field
from django import forms
from .models import Message, Consultation


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message

        fields = ["name", "email", "message"]


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation

        fields = ["first_name", "last_name", "email", "phone",
        "job_title", "company_name", "website", "message"]