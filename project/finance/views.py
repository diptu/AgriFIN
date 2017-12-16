from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView, DetailView, FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import *
from .models import *


from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


from social_django.models import UserSocialAuth

class HomePageView(TemplateView):

    template_name = "home.html"


@login_required
def settings(request):
    user = request.user


    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None



    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'finance/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'finance/password.html', {'form': form})

# @login_required
# def profile(request):
#     # print(request.session)
#     template_name = 'finance/user_detail1.html'
#     user = get_object_or_404(User, username=request.user)
#     # queryset = get_object_or_404(User, id = request.user.id)
#     # print(request.user.id)
#     user.status = 1
#     context = {
#         "object_list": user
#     }
#     print(user.status)
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

class HistoryListView(ListView):
    model = Land
    def get_queryset(self):
        if self.request.user.status == 2:
            queryset = Share.objects.filter(investor = self.request.user)
        elif self.request.user.status == 1:
            queryset = Land.objects.filter(owner = self.request.user)

        # print(queryset)
        return queryset

class BranchListView(ListView):
    model = Branch

class CropListView(ListView):
    model =Crop



class StatusChoice():
    def choices(a):
        STATUS_CHOICES = {1: "Farmer", 2: "Investor", 3: "Employee"}
        return STATUS_CHOICES[a]

class UserDetail(LoginRequiredMixin, DetailView):
    template_name = 'finance/user_detail.html'
    def get_object(self, *args, **kwargs):
        context = get_object_or_404(User, id=self.request.user.id) # pk = rest_id
        context.status = StatusChoice.choices(context.status)
        return context



class ProfileUpdateView(UserPassesTestMixin, FormView):
    def test_func(self):
        return self.request.user.status == 2

    template_name = 'finance/profile_update.html'
    form_class    = ProfileUpdate
    success_url   = 'profile'

    def form_valid(self, form):
        #print(request.user.status)
        if form.is_valid():
            #first_name      = form.cleaned_data.get('first_name')
            #last_name       = form.cleaned_data.get('last_name')
            bio             = form.cleaned_data.get('bio')
            location        = form.cleaned_data.get('location')
            email        = form.cleaned_data.get('email')


            User.objects.update(#first_name = first_name,
                                #last_name = last_name,
                                location=location,
                                email=email,
                                bio =bio)
        return redirect('profile')


class LandUpdateView(UserPassesTestMixin, FormView):
    def test_func(self):
        return self.request.user.status == 3

    template_name = 'finance/land_update.html'
    form_class    = LandUpdate
    success_url   = 'profile'

    def form_valid(self, form):
        #print(request.user.status)
        if form.is_valid():
            worker = form.cleaned_data.get('worker_fee')
            irrigation = form.cleaned_data.get('irrigation_fee')
            other = form.cleaned_data.get('other_cost')
            budget = Budget.objects.create(worker_fee=worker,
                                            irrigation_fee=irrigation,
                                            other_cost=other)


            owner          = form.cleaned_data.get('owner')
            location       = form.cleaned_data.get('location')
            share_price    = form.cleaned_data.get('share_price')
            share_quantity = form.cleaned_data.get('share_quantity')
            #total_share    = form.cleaned_data.get('share_quantity')
            fertility_rate = form.cleaned_data.get('fertility_rate')

            Land.objects.create(budget = budget,
                                owner=owner,
                                location=location,
                                share_price=share_price,
                                share_quantity=share_quantity,
                                total_share=share_quantity,
                                fertility_rate=fertility_rate)
        return redirect('profile')

class RevenueView(UserPassesTestMixin, FormView, DetailView):
    def test_func(self):
        return self.request.user.status == 3

    template_name = 'finance/revenue.html'
    form_class    = RevenueForm
    success_url   = 'profile'

    def form_valid(self, form):
        if form.is_valid():
            quantity  = form.cleaned_data.get('total_revenue')
            land      = Land.objects.get(id = self.kwargs.get('id'))
            shared    = Share.objects.filter(land = land)
            for i in shared:
                value = i.investor.account + (quantity * i.percentage)/100
                User.objects.filter(id = i.investor.id).update(account = value)
                print(value)
                i.delete()
                # print((quantity * i.percentage)/100)
            return redirect('profile')
    def get_object(self, *args, **kwargs):
        # context = get_object_or_404(User, id=self.request.user.id) # pk = rest_id
        context = Land.objects.get(id = self.kwargs.get('id'))
        # context.status = StatusChoice.choices(context.status)
        return context

class BuyShareView(UserPassesTestMixin, FormView):
    def test_func(self):
        return self.request.user.status == 2

    template_name = 'finance/action_page.html'
    form_class    = BuyShare
    success_url   = 'profile'

    def form_valid(self, form):
        if form.is_valid():
            # work = form.save()
            # land_id = form.cleaned_data.get('land_id')
            land = Land.objects.get(id = self.kwargs.get('id'))
            # user_id = form.cleaned_data.get('user_id')
            user = User.objects.get(id=self.request.user.id)
            # print(self.kwargs.get('id'))
            quantity = form.cleaned_data.get('quantity')
            # percentage = land.total_share -(Share.amount)
            # print(percentage)

            land.share_quantity -= quantity

            land.share_sold   = ((land.total_share-land.share_quantity)/(land.total_share))*100

            if Share.objects.filter(investor = user, land = land).exists():
                data = Share.objects.get(investor = user, land = land)
                new_amount = data.amount + quantity
                Share.objects.filter(investor = user, land = land).update(amount = new_amount)
                percent   = 100 - ((land.total_share - new_amount)/(land.total_share))*100
                Share.objects.filter(investor = user, land = land).update(percentage = percent)

            else:
                data = Share(investor = user, land = land, amount = quantity)
                data.percentage   = 100 - ((land.total_share - data.amount)/(land.total_share))*100
                data.save()

            print(Share.objects.get(investor = user, land = land).percentage)
            land.save()
        return redirect('profile')

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
