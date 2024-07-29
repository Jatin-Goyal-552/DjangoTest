from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *


def signin(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(name, email, password)
        return render(request, 'login.html')
    
    return render(request, 'registration.html')

def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        print("name", name, password)
        user = User.objects.filter(username=name, password=password).first()
        if user:
            return render(request, 'home.html')
    
    return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')


def upload_image(request):
    initial_data = {
        'user': request.user,
    }
    form = ImageForm(initial=initial_data)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, initial=initial_data)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('upload_image')
    context = {'form': form}
    return render(request, 'upload_image.html', context)