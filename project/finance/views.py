<<<<<<< HEAD
from django.db.models import Q
from django.shortcuts import render
from .models import *

# Create your views here.
from django.views.generic import TemplateView, ListView

def home(request):
    return render(request, "home.html", {})

def login(request):
    return render(request, "login.html", {})



def profile(request):
    return render(request, "profile.html", {})

def signup(request):
    return render(request, "signup.html", {})

# def land_profile(request):
#     template_name = 'finance/market.html'
#     queryset = Land.objects.all()
#     context = {
#         "object_list" : queryset
#     }
#     return render(request, template_name, context)

class FarmerProfileListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Farmer.objects.filter(
                    Q(full_name__iexact=slug) |
                    Q(full_name__icontains=slug)
                )
        else:
            queryset = Farmer.objects.all()
        return queryset


class InvestorProfileListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Investor.objects.filter(
                    Q(full_name__iexact=slug) |
                    Q(full_name__icontains=slug)
                )
        else:
            queryset = Investor.objects.all()
        return queryset


class LandListView(ListView):
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Land.objects.filter(
                    Q(location__iexact=slug) |
                    Q(location__icontains=slug)
                )
        else:
            queryset = Land.objects.all()
        return queryset
=======
from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'signup.html', {})

def home(request):
    return render(request, "home.html", {})
>>>>>>> 20eb7e3bb2e7cbacc099e1e04e2f96eb6b410657
