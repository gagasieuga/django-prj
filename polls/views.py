from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render (request, 'pages/home.html')
def base(request):
    return render (request, 'pages/base.html')
def contact(request):
    return render (request, 'pages/contact.html')
def error_404_view(request, exception):
    return render(request,'pages/404.html')
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid(): # if form is valid with all the methods inside the form.py
            form.save()
            return HttpResponse("User Registered Successfully")
    return render(request, 'pages/register.html', {'form': form})