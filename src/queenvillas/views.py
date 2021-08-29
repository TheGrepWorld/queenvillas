from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from account.models import UserAccount
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from residential.models import ResidentialDetails


def home_page(request):
    residential_data = ResidentialDetails.objects.all()
    context = {
        'residential_data': residential_data
    }
    return render(request, 'home_page.html', context)


def handle_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        phoneno = request.POST['phoneno']
        fullname = fname + " " + lname
        if not username.isalnum():
            messages.error(request, "Username should only contains letters and numbers")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        UserAccount.objects.create(full_name=fullname, phoneno=phoneno, email=email)
        messages.success(request, "Your account has been successfully created")

        return redirect('home')
    else:
        return HttpResponse('404 - Not Allowed')


def handle_login(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
        else:
            messages.ERROR(request, "Invalid credentials")
            return redirect('home')

    return HttpResponse('404-Not Found')


def handle_logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
