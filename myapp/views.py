from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import *

# Create your views here.

@csrf_exempt
def addproduct_get(request):
    a = Product.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        p = Product()
        p.name = name
        p.price = price
        p.save()
    return render(request,'add_product.html',{'data':a})