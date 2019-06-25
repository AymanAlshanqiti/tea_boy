from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Item
from .models import Order



def items_list(request):
    context = {
        "items": Item.objects.all()
    }
    return render(request, 'items_list.html', context)


def order_create(request):

    user = User.objects.get(id=1)
    selected_item = request.POST.get('item-name')
    item = Item.objects.get(name = selected_item)
    orders = Order.objects.all()
    print(user)

    context = {
        "orders": orders,
        "item": item
    }
    return render(request, 'orders.html', context)