from django.shortcuts import render, redirect
from .models import Services, Work, Consultation
from .forms import ContactForm, ConsultationForm
from django.contrib import messages

# Create your views here.

def home(request):
    works = Work.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            # username = form.cleaned_data.get('name')
            # email = form.cleaned_data.get('email')
            # message = form.cleaned_data.get('message')
            form.save()
            
            # messages.success(request, f"Hi {username} your message has been received.")
            return redirect('home')

    else:
        form = ContactForm()
    context = {
        'form': form,
        'works': works
    }
    return render(request, 'content/home.html', context)


def index(request):
    works = Work.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            # username = form.cleaned_data.get('name')
            # email = form.cleaned_data.get('email')
            # message = form.cleaned_data.get('message')
            form.save()
            
            # messages.success(request, f"Hi {username} your message has been received.")
            return redirect('home')

    else:
        form = ContactForm()
    context = {
        'form': form,
        'works': works
    }
    return render(request, 'content/index.html', context)



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



def consult(request):
    if request.method == "POST":
        form = ConsultationForm(request.POST)

        if form.is_valid():
            # first_name = form.cleaned_data.get("first_name")
            # last_name = form.cleaned_data.get("last_name")
            # email = form.cleaned_data.get("email")
            # phone = form.cleaned_data.get("phone")
            # job_title = form.cleaned_data.get("job_title")
            # compamy_name = form.cleaned_data.get("company_name")
            # website = form.cleaned_data.get("website")
            # message = form.cleaned_data.get("message")
            # form.save()
            first_name = request.POST["first_name"]
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            job_title = request.POST.get("job_title")
            company_name = request.POST.get("company_name")
            website = request.POST.get("website")
            message = request.POST.get("message")

            consultation = Consultation.objects.create(first_name=first_name, last_name=last_name, email=email,
            phone=phone, job_title=job_title, company_name=company_name, website=website, message=message)
            consultation.save()
            messages.success(request, f"Hi {first_name}, you have successfully booked a session with us. Check your mail for more details")
            return redirect('home')

    else:
        form = ConsultationForm()

    context = {
        "form": form,
    }

    return render(request, 'content/consultation.html', context)