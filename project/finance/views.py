from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q
from django.shortcuts import render
from .models import *

from .forms import FarmerCreateForm

# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView

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

class FarmerCreateView(LoginRequiredMixin, CreateView):
    form_class = FarmerCreateForm
    login_url = '/login/'
    template_name = 'finance/form.html'
    success_url = "/home/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(FarmerCreateView, self).form_valid(form)
