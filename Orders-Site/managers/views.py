from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from items.models import Category,Dish
from orders.models import Delivery,Cart
from users.models import User

# Create your views here.

# Users - Managers

def manager_login(request):
    if request.method == 'POST':
        manager = authenticate(request,
                           username=request.POST['username'],
                           password=request.POST['password']
                           )
        if manager is not None:
            if manager.is_staff:
                login(request,manager)
                return redirect('main-page')
            else:
                messages.error(request,f'Hello {manager}, you have been redirected to log in through normal users login page. Please log in again.')
                return redirect('user-login')
        elif User.objects.filter(username=request.POST['username']).exists():
            messages.error(request,'wrong password.')
            return redirect('manager-login')
        else:
            messages.error(request,'no username with this name found.')
            return redirect('user-login')
    else:
        return render(request,'managers/manager_login.html')

@login_required(login_url='manager-login')
def manage_users(request):
    if request.user.is_staff:
        users = User.objects.all()
        return render(request,'managers/users/manage_users.html',{'users':users})
    else:
        return redirect('manager-login')

@login_required(login_url='manager-login')    
def make_manager(request,id):
    if request.user.is_staff:
        user = User.objects.get(id=id)
        user.is_staff = True
        user.save()
        return redirect('manage-users')
    else:
        return redirect('manager-login')
    
@login_required(login_url='manager-login')    
def cancel_manager(request,id):
    if request.user.is_staff:
        user = User.objects.get(id=id)
        if user == request.user:
            messages.error(request,"You can't cancel your own permissions, you can only cancel other managers permissions.")
            return redirect('manage-users')
        user.is_staff = False
        user.save()
        return redirect('manage-users')
    else:
        return redirect('manager-login')
    
@login_required(login_url='manager-login')    
def delete_user(request,id):
    if request.user.is_staff:
        user = User.objects.get(id=id)
        if request.method == 'POST':
            carts = Cart.objects.filter(profile_id = user,is_done=True)
            if carts.exists():
                for cart in carts:
                    delivery = Delivery.objects.get(cart=cart)
                    delivery.delete()
                    cart.delete()
            try:
                cart = Cart.objects.get(profile_id = user,is_done=False)
                cart.delete()
            except:
                pass
            user.delete()
            return redirect('manage-users')
        else:
            return render(request,'managers/users/delete_user.html',{'user':user})
    else:
        return redirect('manager-login')

@login_required(login_url='manager-login')
def edit_user(request,id):
    if request.user.is_staff:
        user = User.objects.get(id=id)
        if request.method == 'POST':
            user.username = request.POST['username']
            user.password = make_password(request.POST['password'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            if request.POST.get('is_staff'):
                user.is_staff = True
            else:
                user.is_staff = False
            user.save()
            return redirect('manage-users')
        return render(request,'managers/users/edit_user.html',{"user":user})
    else:
        return redirect('manager-login')

# Categories - Managers

@login_required(login_url='manager-login')
def manage_categories(request):
    if request.user.is_staff:
        categories = Category.objects.all()
        return render(request,'managers/categories/manage_categories.html',{'categories':categories})
    else:
        return redirect('manager-login')
    
@login_required(login_url='manager-login')
def manage_category(request,id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.imageUrl = request.POST['imageUrl']
        category.save()
        return redirect('manage-categories')
    return render(request,'managers/categories/manage_category.html',{'category':category})

@login_required(login_url='manager-login')
def delete_cat(request,id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('manage-categories')
    
@login_required(login_url='manager-login')
def add_category(request):
    if request.method == 'POST':
        new_cat = Category(
            name = request.POST['name'],
            imageUrl= request.POST['imageUrl']
        )
        new_cat.save()
        return redirect('manage-categories')
    return render(request,'managers/categories/add_category.html')

# Dishes - Managers

@login_required(login_url='manager-login')
def manage_dishes(request):
    if request.user.is_staff:
        dishes = Dish.objects.all()
        return render(request,'managers/dishes/manage_dishes.html',{'dishes':dishes})
    else:
        return redirect('manager-login')
    
@login_required(login_url='manager-login')    
def manage_dishes_by_cat(request,id):
    if request.user.is_staff:
        category = Category.objects.get(id=id)
        dishes = category.dish_set.all()
        return render(request,'managers/dishes/manage_dishes_by_cat.html',{'dishes':dishes})
    else:
        return redirect('manager-login')
    
@login_required(login_url='manager-login') 
def manage_dish(request,id):
    if request.user.is_staff:
        categories = Category.objects.all()
        dish = Dish.objects.get(id=id)
        if request.method == 'POST':
            dish.name = request.POST['name']
            dish.price = request.POST['price']
            dish.description = request.POST['description']
            dish.imageUrl = request.POST['imageUrl']
            dish.category = Category.objects.get(id=request.POST['category'])
            if request.POST.get('is_gluten_free'):
                dish.is_gluten_free = True
            else:
                dish.is_gluten_free = False
            if request.POST.get('is_vegeterian'):    
                dish.is_vegeterian = True
            else:
                dish.is_vegeterian = False
            dish.save()
            return redirect('manage-dishes')
        
        return render(request,'managers/dishes/manage_dish.html',{'dish':dish,'categories':categories})
    else:
        return redirect('manager-login')

@login_required(login_url='manager-login')
def add_dish(request):
    if request.user.is_staff:
        categories = Category.objects.all()
        if request.method == 'POST':
            new_dish = Dish(
                name=request.POST['name'],
                price = request.POST['price'],
                description = request.POST['description'],
                imageUrl = request.POST['imageUrl'],
                category = Category.objects.get(id=request.POST['category'])
            )       
            if request.POST.get('is_gluten_free'):
                new_dish.is_gluten_free = True
            
            if request.POST.get('is_vegeterian'):    
                new_dish.is_vegeterian = True

            new_dish.save()
            return redirect('manage-dishes')
        
        return render(request,'managers/dishes/add_dish.html',{'categories':categories})
    else:
        return redirect('manager-login')
    
@login_required(login_url='manager-login')
def delete_dish(request,id):
    if request.user.is_staff:
        dish = Dish.objects.get(id=id)
        if request.method == 'POST':
            dish.delete()
            return redirect('manage-dishes')    
    else:
        return redirect('manager-login')
    
# Deliveries - managers

@login_required(login_url='manager-login')
def manage_deliveries(request):
    if request.user.is_staff:
        delivs = Delivery.objects.all()
        return render(request,'managers/deliveries/manage_deliveries.html',{'deliveries':delivs})
    else:
        return redirect('manager-login')
    
@login_required(login_url='manager-login')
def delivery_by_id(request):
    if request.user.is_staff:
        if request.method == 'POST':
            try:
                cart = Cart.objects.get(id=request.POST['order_id'],is_done=True)
            except:
                messages.error(request,'Couldnt find a matching delivery, or delivery is not done yet.')
                return redirect('manage-deliveries')
            user = cart.profile_id
            delivery = Delivery.objects.get(cart=cart)
            return render(request,'managers/deliveries/delivery_by_id.html',{'user':user,'cart':cart,'delivery':delivery})
        return redirect('manage-deliveries')
    else:
        return redirect('manager-login')
    
@login_required(login_url='manager-login')
def delivery_by_arrived(request):
    if request.user.is_staff:
        deliveries = Delivery.objects.filter(is_delivered=True)
        if deliveries.exists():
            return render(request,'managers/deliveries/by_arrived.html',{'deliveries':deliveries})
        else:
            deliveries = False
            messages.error(request,'All deliveries are on there way.')
            return render(request,'managers/deliveries/by_arrived.html',{'deliveries':deliveries})
    else:
        return redirect('manager-login')
    
@login_required(login_url='manager-login')
def delivery_by_not_arrived(request):
    if request.user.is_staff:
        deliveries = Delivery.objects.filter(is_delivered=False)
        if deliveries.exists():
            return render(request,'managers/deliveries/by_not_arrived.html',{'deliveries':deliveries})
        else:
            deliveries = False
            messages.error(request,'All deliveries arrived.')
            return render(request,'managers/deliveries/by_not_arrived.html',{'deliveries':deliveries})
    else:
        return redirect('manager-login')
    
@login_required(login_url='manager-login')
def check_arrived(request,id):
    if request.user.is_staff:
        delivery = Delivery.objects.get(cart=Cart.objects.get(id=id))
        delivery.is_delivered = True
        delivery.save()
        return redirect('manage-deliveries')
    else:
        return redirect('manager-login')
    
@login_required(login_url='manager-login')
def delete_delivery(request,id):
    if request.user.is_staff:
        cart =Cart.objects.get(id=id)
        delivery = Delivery.objects.get(cart=cart)
        delivery.delete()
        cart.delete()
        return redirect('manage-deliveries')
    else:
        return redirect('manager-login')
    
@login_required(login_url='manager-login')
def mark_unarrived(request,id):
    if request.user.is_staff:
        delivery = Delivery.objects.get(cart=Cart.objects.get(id=id))
        delivery.is_delivered = False
        delivery.save()
        return redirect('manage-deliveries')
    else:
        return redirect('manager-login')
    
# Manager / Carts

@login_required(login_url='manager-login')
def manage_carts(request):
    if request.user.is_staff:
        carts = Cart.objects.filter(is_done=True)
        return render(request,'managers/carts/manage_carts.html',{'carts':carts})
    
@login_required(login_url='manager-login')
def carts_by_user_id(request):
    if request.user.is_staff:
        if request.method == 'POST':
            try:
                user = User.objects.get(id=request.POST['id'])
            except:
                messages.error(request,'Couldnt found a matching username,please try again.')
                return redirect('manage-carts')
            carts = Cart.objects.filter(profile_id=user,is_done=True)
            has_carts = True if carts.exists() else False
            deliveries = []
            for cart in carts:
                delivery = Delivery.objects.get(cart=cart)
                deliveries.append(delivery)
            return render(request,'managers/carts/carts_by_user_id.html',{'user':user,'carts':carts,'deliveries':deliveries,'has_carts':has_carts})
        return redirect('manage-carts')
    else:
        return redirect('manager-login')
        
    
@login_required(login_url='manager-login')
def carts_by_username(request):
    if request.user.is_staff:
        if request.method == 'POST':
            try:
                user = User.objects.get(username=request.POST['username'])
            except:
                messages.error(request,'Couldnt found a matching user,please try again.')
                return redirect('manage-carts')
            carts = Cart.objects.filter(profile_id=user,is_done=True)
            has_carts = True if carts.exists() else False
            deliveries = []
            for cart in carts:
                delivery = Delivery.objects.get(cart=cart)
                deliveries.append(delivery)
            return render(request,'managers/carts/carts_by_username.html',{'user':user,'carts':carts,'deliveries':deliveries,'has_carts':has_carts})
        return redirect('manage-carts')
    else:
        return redirect('manager-login')
    
@login_required(login_url='manager-login')
def cart_by_id(request):
    if request.user.is_staff:
        if request.method == 'POST':
            try:
                cart = Cart.objects.get(id=request.POST['order_id'],is_done=True)
            except:
                messages.error(request,'Couldnt found a matching cart, or cart is not done yet.')
                return redirect('manage-carts')
            user = cart.profile_id
            delivery = Delivery.objects.get(cart=cart)
            return render(request,'managers/carts/cart_by_id.html',{'user':user,'cart':cart,'delivery':delivery})
        return redirect('manage-carts')
    else:
        return redirect('manager-login')
    
@login_required(login_url='manager-login')
def delete_cart(request,id):
    if request.user.is_staff:
        cart =Cart.objects.get(id=id)
        delivery = Delivery.objects.get(cart=cart)
        delivery.delete()
        cart.delete()
        return redirect('manage-carts')
    else:
        return redirect('manager-login')