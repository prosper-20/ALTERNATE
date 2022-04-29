from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Oops, email is already connected to another account")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                user.save()
                messages.info(request, "Your account has been created successfully")
                return redirect("home")
        else:
            messages.info(request, "Both passowrds do not match")
            # You just it from register.html to form-regsiter
    return render(request, 'users/register.html')

# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             # messages.success(request, "You are logged in")
#             return redirect('/')
#         else:
#             messages.error(request, "Credentials not valid")
#             return redirect("login")
#     #You changed from login.htnl to form-login
#     return render(request, 'login.html')

# def logout(request):
#     auth.logout(request)
#     return render(request, 'logout.html')


