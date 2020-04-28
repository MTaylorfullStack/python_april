from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    print("This is my first response!")
    return render(request, 'index.html')

def goodbye(request):
    return render(request, 'goodbye.html')

def name(request, name):
    context = {
        'key': "Value!!!",
        'name': name
    }
    return render(request, 'name.html', context)