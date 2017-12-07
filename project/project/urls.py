"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from finance.views import *




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    
    url(r'^$', home, name='home'),
    # url(r'^login/$',auth_views.login, name='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'finance/login.html'}, name='login'),
    url(r'^signup/$', signup, name='signup'),
    # url(r'^profile/$',profile),
    url(r'^update/$',ProfileUpdateView.as_view()),
    url(r'^profile/$',UserDetail.as_view(), name='profile'),
    url(r'^profile/history/$',HistoryListView.as_view()),

    url(r'^add/$',LandUpdateView.as_view()),


    url(r'^branch/$',BranchListView.as_view()),
    url(r'^branch/(?P<id>\d+)/$', BranchDetail.as_view()),
    url(r'^market/(?P<id>\d+)/$', LandDetail.as_view()),
    url(r'^market/$',LandListView.as_view()),

    url(r'^crop/$',CropListView.as_view()),
    url(r'^crop/(?P<id>\d+)/$', CropDetail.as_view()),
    url(r'^fertilizer/$',FertilizerListView.as_view()),
    url(r'^fertilizer/(?P<id>\d+)/$', FertilizerDetail.as_view()),
    url(r'^market/(?P<id>\d+)/buyshare/$', BuyShareView.as_view()),
    url(r'^contact/$',TemplateView.as_view(template_name='contact.html')),
    url(r'^about/$',TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),


]
