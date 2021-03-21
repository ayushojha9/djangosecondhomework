from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class indexView(TemplateView):
        template_name="index.html"

class aboutView(TemplateView):
        template_name="about.html"


class loginView(TemplateView):
        template_name="login.html"

class registerView(TemplateView):
        template_name="register.html"

class productsView(TemplateView):
        template_name="products.html"
