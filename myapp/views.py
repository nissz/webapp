
from django.shortcuts import render, redirect
from .models import  user
def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        Email = request.POST.get("Email")
        password = request.POST.get("password")
        user(username=username, Email=Email, password=password).save()
        return redirect('login')
    return render(request, "register.html")
def login(request):
    if request.method == "POST":
        Email = request.POST.get("Email")
        password = request.POST.get("password")
        users=user.objects.filter(Email=Email,password=password)
        if users:
            return redirect('profile')
    else:
        return render(request, "login.html")

def profile(request):
        return render(request,"profile.html")