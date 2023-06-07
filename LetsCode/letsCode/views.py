from django.shortcuts import render


def login(request):
    return render(request,'letscode/login.html')

def home(request):
    return render(request,'letscode/home.html')

def register(request):
    return render(request,'letscode/register.html')