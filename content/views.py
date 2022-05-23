from django.shortcuts import render, redirect
from .models import Services, Work, Consultation, Gallery
from blog.models import Post
from .forms import ContactForm, ConsultationForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail
from sendgrid.helpers.mail import SandBoxMode, MailSettings

# Create your views here.

def home(request):
    works = Work.objects.all()
    posts = Post.objects.all()
    services = Services.objects.all()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('name')
            # email = form.cleaned_data.get('email')
            # message = form.cleaned_data.get('message')
            form.save()
            
            messages.success(request, f"Hi {username} your message has been received.")
            return redirect('home')

    else:
        form = ContactForm()
    context = {
        'form': form,
        'works': works,
        "posts": posts,
        "services": services
    }
    # You chnaged this from home.html to index.html
    return render(request, 'content/content_index.html', context)


# def index(request):
#     works = Work.objects.all()
#     if request.method == "POST":
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             # username = form.cleaned_data.get('name')
#             # email = form.cleaned_data.get('email')
#             # message = form.cleaned_data.get('message')
#             form.save()
            
#             # messages.success(request, f"Hi {username} your message has been received.")
#             return redirect('home')

#     else:
#         form = ContactForm()
#     context = {
#         'form': form,
#         'works': works
#     }
#     return render(request, 'content/index.html', context)



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
            mydict = {'first_name': first_name}
            html_template = 'content/consultation_email.html'
            html_message = render_to_string(html_template, context=mydict)
            subject = 'Booking Session Confirmation'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            message = EmailMessage(subject, html_message,
                                   email_from, recipient_list)
            message.content_subtype = 'html'
            message.send()
            messages.success(request, f"Hi {first_name}, you have successfully booked a session with us. Check your mail for more details")
            return redirect('home')

    else:
        form = ConsultationForm()

    context = {
        "form": form,
    }

    return render(request, 'content/consultation.html', context)


def about(request):
    return render(request, "content/about_us.html")


def gallery(request):
    gallery = Gallery.objects.all()
    context = {
        "gallery": gallery
    }
    return render(request, "content/gallery.html", context)


