
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse
from django.urls import path

from myapp import views


def home(request):
    return HttpResponse("Server is running bro 🚀")

urlpatterns = [
    path('', home),
    path('add_product/', views.addproduct_get),
    path('getmessage/', views.getmessage),
    path('sendmessage/', views.sendmessage),
]
