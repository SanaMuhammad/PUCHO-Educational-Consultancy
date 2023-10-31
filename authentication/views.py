from django.contrib import auth
from django.core.checks import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from fyp_pucho import settings


def login_view(request):
    msg = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/form")
        else:
            msg = 'Invalid credentials'


    return render(request, "login.html", {"msg" : msg})

def register_user(request):
    msg = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        # User.objects.create_user(username=username, password=password, email=email)
        msg     = 'User created.'
        success = True
    #     return redirect('/form')
    # else:
    #     msg = 'Form is not valid'
        if User.objects.create_user(username=username, password=password, email=email):
            return redirect("/login")
        else:
            msg = 'Form is not valid'

    return render(request, "register.html", {"msg" : msg})

class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect('home')

