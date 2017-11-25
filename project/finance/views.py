from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import SignUpForm, BuyShare
from .models import *

def home(request):
    return render(request, "home.html", {})

# @login_required
# def profile(request):
#     print(request.session)
#     template_name = 'finance/user_detail.html'
#     queryset = User.objects.filter(username=request.user)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, template_name, context)



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            work = form.save()
            work.refresh_from_db()
            work.first_name = form.cleaned_data.get('first_name')
            work.last_name = form.cleaned_data.get('last_name')
            work.status = form.cleaned_data.get('status')
            work.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=work.username, password=raw_password)
            # user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

class LandListView(ListView):
    model = Land

class BranchListView(ListView):
    model = Branch
class CropListView(ListView):
    model =Crop



class StatusChoice():
    def choices(a):
        STATUS_CHOICES = {1: "Farmer", 2: "Investor", 3: "Employee"}
        return STATUS_CHOICES[a]

class UserDetail(LoginRequiredMixin, DetailView):
    # template_name = 'finance/user_detail.html'
    def get_object(self, *args, **kwargs):
        context = get_object_or_404(User, id=self.request.user.id) # pk = rest_id
        context.status = StatusChoice.choices(context.status)
        return context
    # model = User
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(UserDetail, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     # context['book_list'] = Book.objects.all()
    #     print(context)
    #     return context


class BuyShareView(UserPassesTestMixin, FormView):
    def test_func(self):
        return self.request.user.status == 2

    template_name = 'finance/action_page.html'
    form_class = BuyShare
    success_url = 'about'

    def form_valid(self, form):
        if form.is_valid():
            # work = form.save()
            # land_id = form.cleaned_data.get('land_id')
            land = Land.objects.get(id = self.kwargs.get('id'))
            # user_id = form.cleaned_data.get('user_id')
            user = User.objects.get(id=self.request.user.id)
            # print(self.kwargs.get('id'))
            quantity = form.cleaned_data.get('quantity')
            # print(quantity)
            Share.objects.create(investor = user, land = land, amount = quantity)
        return redirect('about')

class LandDetail(DetailView):
    model = Land
    def get_object(self, *args ,**kwargs):
        context = get_object_or_404(Land, id = self.kwargs.get('id'))
        return context

class BranchDetail(DetailView):
    model = Branch
    def get_object(self, *args, **kwargs):
        branch_id = self.kwargs.get('id')
        obj = get_object_or_404(Branch, id=branch_id) # pk = rest_id
        return obj


class CropDetail(DetailView):
    model = Crop
    def get_object(self, *args, **kwargs):
        crop_id = self.kwargs.get('id')
        obj = get_object_or_404(Crop, id=crop_id) # pk = rest_id
        return obj


class FertilizerListView(ListView):
    model = Fertilizer

class FertilizerDetail(DetailView):
    model = Fertilizer
    def get_object(self, *args, **kwargs):
        fertilizer_id = self.kwargs.get('id')
        obj = get_object_or_404(Fertilizer, id=fertilizer_id) # pk = rest_id
        return obj
