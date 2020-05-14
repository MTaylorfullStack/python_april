from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'index.html')

def success(request):
    if 'name' in request.session:
        return render(request, 'success.html')
    return redirect('/')

def register(request):
    print(request.POST)
    # validate the post data
    errors = User.objects.validator(request.POST)
    print(errors)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    hashed_password = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password=hashed_password)
    # create a new User
    print(new_user, "This is my new user!")
    request.session['name'] = new_user.first_name
    return redirect('/success')

def login(request):
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user)>0:
        logged_user = logged_user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            print(logged_user, "logged user was signed in!")
            request.session['name'] = logged_user.first_name
            return redirect('/success')

    # see if POST data matches a User from db
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')
