"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firsthomework import views
from firsthomework.views import indexView
from firsthomework.views import aboutView
from firsthomework.views import loginView
from firsthomework.views import registerView
from firsthomework.views import productsView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',indexView.as_view()),
    path('about',aboutView.as_view()),
    path('login',loginView.as_view()),
    path('register',registerView.as_view()),
    path('products',productsView.as_view()),
]
