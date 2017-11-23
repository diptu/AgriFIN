from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, 'signup.html', {})

def home(request):
    return render(request, "home.html", {})
