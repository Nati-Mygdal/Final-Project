from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart,Delivery
from items.models import Item,Dish
from utils import get_total

# Create your views here.

@login_required(login_url='user-login')
def show_cart(request,id):
    user = request.user
    try:
        cart = Cart.objects.get(profile_id=user,is_done=False)
        items = Item.objects.filter(cart=cart)
        total = get_total(items)
    except:
        cart = Cart(
        profile_id = user
        )
        cart.save()
        total = 0
    items = Item.objects.filter(cart_id=cart)

    if request.method == 'POST':
        if len(request.POST['phone']) != 10:
            messages.error(request,"Phone number must be 10 digits long.")
            return redirect('show-cart',id=user.id)
        if not (request.POST['phone']).isdigit():
            messages.error(request,"Phone number can't include letters.")
            return redirect('show-cart',id=user.id)
        cart_item = Item.objects.filter(cart=cart)
        if not cart_item:
            messages.error(request, "You can't send an empty cart.")
            return redirect('show-cart',id=user.id)
        else:
            new_del = Delivery(
                address = request.POST['address'],
                comment = request.POST['comment'],
                phone = request.POST['phone'],
                cart = cart
            )
            new_del.save()
            cart.is_done = True
            cart.save()
            messages.success(request,"Success! Delivery is on its way.")
            return redirect('order-info',id=id)
    return render(request,'orders/show_cart.html',{'total':total,'items':items})


@login_required(login_url='user-login')
def history(request,id):
    carts = Cart.objects.filter(profile_id=id,is_done=True)
    has_orders = True if carts.exists() else False
    deliveries = []
    for cart in carts:
        delivery = Delivery.objects.get(cart=cart)
        deliveries.append(delivery)
    return render(request,'orders/carts_history.html',{'carts':carts,'deliveries':deliveries,'has_orders':has_orders})

@login_required(login_url='user-login')
def information(request,id):
    cart = Cart.objects.filter(profile_id=id).last()
    items = Item.objects.filter(cart=cart)
    total = get_total(items)
    delivery = Delivery.objects.get(cart=cart)
    return render(request,'deliveries/delivery_info.html',{'delivery':delivery,'total':total,'items':items})

@login_required(login_url='user-login')
def add_to_cart(request,id):
    user = request.user
    if request.method == 'POST':  
        try:
            cart = Cart.objects.get(profile_id=user.id,is_done=False)
        except:
            cart = Cart(
                profile_id = user
            )
            cart.save()
        dish = Dish.objects.get(id=id)
        new_item = Item(
            dish = dish,
            cart = cart,
            amount = request.POST['amount']
        )
        new_item.save()
        # Get the URL of the referring page
        referer = request.META.get('HTTP_REFERER')
        # Check if the URL is not None and is within the same domain as the current page
        if referer is not None and referer.startswith(request.scheme + '://' + request.get_host()):
            return redirect(referer)
        else:
            # If the URL is not valid, redirect to the default page
            return redirect('dishes-by-order')
    
@login_required(login_url='user-login')
def delete_from_cart(request,id):
    dish = Dish.objects.get(id=id)
    cart = Cart.objects.get(profile_id=request.user.id,is_done=False)
    item = Item.objects.filter(dish=dish,cart=cart).first()
    item.delete()
    return redirect('show-cart',id=request.user.id)


@login_required(login_url='user-login')   
def re_order(request,id):
    user = request.user
    old_cart = Cart.objects.get(id=id)
    try:
        new_cart = Cart.objects.get(profile_id=user,is_done=False)
    except:
        new_cart = Cart(
            profile_id = user
        )
        new_cart.save()
    for item in old_cart.item_set.all():
        new_item = Item(
            dish = item.dish,
            cart = new_cart,
            amount = item.amount
        )
        new_item.save()
    return redirect('show-cart',id=user.id)
    