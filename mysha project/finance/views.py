from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import *

# Create your views here.
from django.views.generic import TemplateView, ListView

from .forms import *

def person_createview(request):

    if request.method=="POST":
        username = request.POST.get("username")
        password =  request.POST.get("password")
        full_name = request.POST.get("full_name")
        birthday =  request.POST.get("birthday")
        gender  =  request.POST.get("gender")
        profile_picture =  request.POST.get("profile_picture")
        NID = request.POST.get("NID")
        email = request.POST.get("email")
        qualification = request.POST.get("qualificatione")
        mobile_no =request.POST.get("mobile_no")
        address = request.POST.get("address")
        bank_credentials=request.POST.get("bank_credentials")
        title = request.POST.get("title")
        obj=Person.objects.create(
                username=username,
                password=password,
                full_name=full_name,
                birthday=birthday,
                gender=gender,
                profile_picture=profile_picture,
                NID=NID,
                email=email,
                qualification=qualification,
                mobile_no=mobile_no,
                address=address,
                bank_credentials=bank_credentials,
                title=title



            )
        return HttpResponseRedirect("/")


    template_name='finance/form.html'
    context={}
    return render(request,template_name,context)


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
