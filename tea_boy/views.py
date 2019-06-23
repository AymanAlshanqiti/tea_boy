from django.shortcuts import render
from django.http import HttpResponse
from .models import Item


def items_list(request):

    context = {
        "items": Item.objects.all()
    }
    return render(request, 'items_list.html', context)


