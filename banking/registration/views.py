from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('registration:form')
        else:
            messages.info(request,"invalid username or password")
            return redirect('registration:login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        conpassword = request.POST['password2']

        if password==conpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('registration:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('registration:register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                print("user registered")
                return redirect('registration:login')
        else:
            messages.info(request,"password not matching")
            return redirect('registration:register')

    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

def form(request):
    return render(request, "form.html")

def forms(request):
    return render(request, "forms.html" )