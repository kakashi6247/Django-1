from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Account with this username does not exists')

            return redirect('/')
        
        user = authenticate(username = username, password=password)
        if user is None:
            messages.error(request, 'Invalid Credentials')
            return redirect('/')
        else:
            login(request, user)
            return redirect('/overview/')

    return render(request, "login.html", context= {'page' : 'Login'})

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'Username already exists')
            return redirect('/register/')
        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Account with this email already exists')
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username
        )
        user.set_password(password)

        user.save()
        messages.info(request, 'Account created successfully')

        return redirect('/')
    return render(request, "register.html", context= {'page' : 'Register'})

def success_page(request):
    return render(request, "success.html", context= {'page': 'Login Successful'})

@login_required(login_url="/")
def overview(request):
    return render(request, "overview.html", context= {'page': 'Overview'})

@login_required(login_url="/")
def create_feedback(request):
    return render(request, "create_feedback.html", context= {'page': 'Create Feedback'})

@login_required(login_url="/")
def reporting(request):
    return render(request, "reporting.html", context= {'page': 'Reporting'})