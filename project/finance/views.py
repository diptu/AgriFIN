from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from django.views.generic import TemplateView, ListView

def home(request):
    return render(request, "home.html", {})

def profile(request):
    return render(request, "profile.html", {})

def signup(request):

    return render(request, 'signup.html', {})

# def land_profile(request):
#     template_name = 'finance/market.html'
#     queryset = Land.objects.all()
#     context = {
#         "object_list" : queryset
#     }
#     return render(request, template_name, context)

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
