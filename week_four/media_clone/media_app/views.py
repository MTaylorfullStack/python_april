from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, 'index.html')

def feed(request):
    context = {
        'all_posts': Message_Post.objects.all()
    }
    return render(request, 'feed.html', context)

def create_user(request):
    if request.method == 'POST':
        new_user = User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'])
        print(new_user)
        request.session['name'] = new_user.first_name
        request.session['id'] = new_user.id
        return redirect('/feed')
    return redirect('/')

def create_message(request):
    if request.method == 'POST':
        new_mess = Message_Post.objects.create(message=request.POST['contents'], poster=User.objects.get(id=request.session['id']))
        print(new_mess)
        return redirect('/feed')
    return redirect('/')

def like_message(request, id):
    liked_message = Message_Post.objects.get(id=id)
    user_liking = User.objects.get(id=request.session['id'])
    liked_message.likes.add(user_liking)
    return redirect('/feed')

