from django.shortcuts import render

# Create your views here.

def addproduct_get(request):
    return render(request,'add_product.html')