
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("Server is running bro 🚀")

urlpatterns = [
    path('', home),   # 👈 ADD THIS
]
