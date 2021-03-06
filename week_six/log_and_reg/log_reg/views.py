from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'index.html')

def success(request):
    if 'name' in request.session:
        context = {
            'all_messages': Message.objects.all()
        }
        return render(request, 'success.html', context)
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
    request.session['id'] = new_user.id
    return redirect('/success')

def login(request):
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user)>0:
        logged_user = logged_user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            print(logged_user, "logged user was signed in!")
            request.session['name'] = logged_user.first_name
            request.session['id'] = logged_user.id
            return redirect('/success')

    # see if POST data matches a User from db
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')


def create_mess(request):
    if request.method == 'POST':
        new_mess = Message.objects.create(message=request.POST['message'], poster=User.objects.get(id=request.session['id']))
        print(new_mess)
        return redirect('/success')
    return redirect('/')

def add_comm(request, mess_id):
    if request.method == 'POST':
        new_comm = Comment.objects.create(comment=request.POST['comment'], poster=User.objects.get(id=request.session['id']), message=Message.objects.get(id=mess_id))
        print(new_comm)
        return redirect('/success')
    return redirect('/')


def add_like(request, mess_id):
    user_liking = User.objects.get(id=request.session['id'])
    message_liked = Message.objects.get(id=mess_id)
    message_liked.likes.add(user_liking)
    return redirect('/success')

def profile(request, user_id):
    # to view all of the messages and comments this user has posted
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'profile.html', context)

def edit_user(request, user_id):
    # render the edit page
    context = {
        'user': User.objects.get(id=user_id)
    }
    if request.method == 'POST':
        errors = User.objects.validate_edit(request.POST)
        print(errors)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/edit/{str(user_id)}')
        edit_user = User.objects.get(id=user_id)
        edit_user.first_name = request.POST['fname']
        edit_user.last_name = request.POST['lname']
        edit_user.email = request.POST['email']
        edit_user.save()
        return redirect(f'/profile/{str(user_id)}')
    return render(request, 'edit_user.html', context)
    # OR
    # if coming from form submission, process the update

def destroy_mess(request, mess_id):
    one_mess = Message.objects.get(id=mess_id)
    one_mess.delete()
    return redirect('/success')
    
def edit_mess(request, mess_id):
    context = {
        'mess': Message.objects.get(id=mess_id)
    }
    if request.method == 'POST':
        mess = Message.objects.get(id=mess_id)
        mess.message = request.POST['message']
        mess.save()
        return redirect('/success')
    return render(request, 'edit_mess.html', context)
# If I am redirecting to a page that requires an id

# return redirect('/one_mess'+str(mess_id))