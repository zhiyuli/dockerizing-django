import os
from django.shortcuts import render, redirect
from .models import Item
from redis import Redis


redis = Redis(host=os.environ['REDIS_HOST_NAME'], port=os.environ['REDIS_PORT'])


def home(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Item.objects.all()
    counter = redis.incr('counter')
    return render(request, 'home.html', {'items': items, 'counter': counter})
