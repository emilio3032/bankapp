from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404




# Create your views here.

def home(request):
    return render(request, "home.html")



