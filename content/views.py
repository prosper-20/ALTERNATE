from django.shortcuts import render, redirect
from .models import Services
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            form.save()
            messages.success(request, f"Hi {username} your message has been received.")
            return redirect('services')

    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'content/home.html')


def service(request):
    services = Services.objects.all()
    context = {
        'services': services
    }
    return render(request, 'content/services.html', context)


def message(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            form.save()
            messages.success(request, f"Hi {username} your message has been received.")
            return redirect('services')

    else:
        form = ContactForm()
    context = {
        'form': form
    }

    return render(request, 'content/message.html', context)