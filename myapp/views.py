from django.http import JsonResponse
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

@csrf_exempt
def getmessage(request):
    data = Chat.objects.all().order_by('id')

    message_list = []
    for i in data:
        message_list.append({
            'id': i.id,
            'message': i.message,
            'date': i.dateTime.strftime("%Y-%m-%d %H:%M:%S"),
        })

    return JsonResponse({'status': 'ok', 'data': message_list})

from django.utils import timezone
@csrf_exempt
def sendmessage(request):
    try:
        message = request.POST.get('message')

        if not message:
            return JsonResponse({'status': 'error', 'message': 'Message is empty'})

        obj = Chat()
        obj.message = message
        obj.dateTime = timezone.now()   # ✅ FIXED
        obj.save()

        return JsonResponse({'status': 'ok'})

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})