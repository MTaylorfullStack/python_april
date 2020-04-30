from django.shortcuts import render, redirect
import random

def index(request):
    if "feed" not in request.session:
        request.session['feed'] = []
    return render(request, 'index.html')

def process(request):
    print(request.method)
    if request.method == 'POST':
        # play the game
        com_num = int(random.random()*10)
        if int(request.POST['user_guess']) > com_num:
            request.session['result'] = "You guessed too high"
            request.session['feed'].append(request.session['result'])
            request.session['style'] = 'high'
        elif int(request.POST['user_guess']) < com_num:
            request.session['result'] = "You guessed too low"
            request.session['feed'].append(request.session['result'])
            request.session['style'] = 'low'
        else:
            request.session['result'] = "You guessed the number!"
            request.session['feed'].append(request.session['result'])
            request.session['style'] = 'right'
        print(com_num, "This is the com generated number")
        # print(request.POST, "This is my request.POST")
        # print(request.POST['username'])
        # print(request.POST['user_guess'])
        print(request.session['result'], "This was my result")
        return redirect('/')
    return redirect('/')
