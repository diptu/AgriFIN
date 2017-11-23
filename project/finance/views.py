from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from .models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView, DetailView

def home(request):
    return render(request, "home.html", {})

@login_required
def profile(request):
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

class LandDetailView(DetailView):
    queryset = Land.objects.all()

    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get('id')
        obj = get_object_or_404(Land, id=rest_id) # pk = rest_id
        print(obj)
        return obj
