from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Category,Dish,Item
from orders.models import Cart

# Create your views here.


def show_dishes(request,id):
    category = Category.objects.get(id=id)
    categories = Category.objects.all()
    dishes = category.dish_set.all()
    return render(request,'items/show_dishes.html',{'dishes':dishes,"category":category,'categories':categories})

def show_dish_order(request):
    categories = Category.objects.all()
    return render(request,'items/show_dish_order.html',{'categories':categories})

def show_categories(request):
    categories = Category.objects.all()
    return render(request,'items/show_categories.html',{'categories':categories})

