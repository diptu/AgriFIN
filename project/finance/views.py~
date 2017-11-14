from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, "home.html", {})

def login(request):
    return render(request, "login.html", {})



def profile(request):
    return render(request, "profile.html", {})

def signup(request):
    return render(request, "signup.html", {})

def land_profile(request):
    template_name = 'finance/market.html'
    queryset = Land.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request, template_name, context)
