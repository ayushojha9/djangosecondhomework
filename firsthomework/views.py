from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    ctime = datetime.datetime.now()
    return render(request, 'index.html', {'context': ctime})


def about (request):
    ctime = datetime.datetime.now()
    html = "<html><body><h1>this is about page</h1></body></html>"
    return render(request, 'about.html', {'context': ctime})


def register (request):
    ctime = datetime.datetime.now()
    html = "<html><body><h1>this is register page</h1></body></html>"
    return render(request, 'register.html', {'context': ctime})

def login (request):
    ctime = datetime.datetime.now()
    html = "<html><body><h1>this is login page</h1></body></html>"
    return render(request, 'login.html', {'context': ctime})

def products (request):
    ctime = datetime.datetime.now()
    html = "<html><body><h1>this is products page</h1></body></html>"
    return render(request, 'products.html', {'context': ctime})
