from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Item
from .models import Order
from .forms import UserLogin
from django.contrib.auth import authenticate, login, logout




def items_list(request):
    context = {
        "items": Item.objects.all()
    }
    return render(request, 'items_list.html', context)


def orders_list(request):
    context = {
        "orders": Order.objects.all()
    }
    return render(request, 'orders.html', context)


def order_create(request):
    
    selected_item = request.POST.get('item-name')
    item = Item.objects.get(name = selected_item)

    order = Order()
    order.user = request.user
    order.item = item
    order.save()
    return redirect("orders-list")


def user_login(request):
    form = UserLogin()
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect('items-list')

    context = {
        "form":form
    }
    return render(request, 'login.html', context)



def order_delete(request, order_id):
    order = Order.objects.get(id=order_id).delete()
    return redirect('orders-list')


def logout_view(request):
    logout(request)
    return redirect('login')