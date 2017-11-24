from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignUpForm, BuyShare
from .models import *

def home(request):
    return render(request, "home.html", {})

@login_required
def profile(request):
    print(request.session)
    template_name = 'finance/user_detail.html'
    queryset = User.objects.filter(username=request.user)
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)



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


class UserDetail(LoginRequiredMixin, DetailView):
    template_name = 'finance/user_detail.html'
    def get_object(self):
        return self.request.user

class BuyShareView(FormView):
    template_name = 'finance/action_page.html'
    form_class = BuyShare
    success_url = 'about'

    def form_valid(self, form):
        if form.is_valid():
            # work = form.save()
            land_id = form.cleaned_data.get('land_id')
            land = Land.objects.get(id = land_id)
            user_id = form.cleaned_data.get('user_id')
            user = User.objects.get(id = user_id)
            quantity = form.cleaned_data.get('quantity')
            Share.objects.create(investor = user, land = land, amount = quantity)
            print(user)
        return redirect('about')

class LandDetail(DetailView):
    model = Land
    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get('id')
        context = get_object_or_404(Land, id=rest_id) # pk = rest_id
        return context
