from django.shortcuts import render
from .models import *

# Create your views here.

def addproduct_get(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        p = Product()
        p.name = name
        p.price = price
        p.save()
    return render(request,'add_product.html')