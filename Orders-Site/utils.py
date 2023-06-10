from items.models import Category
from users.models import User
import random

#total bill func
def get_total(items):
    total = 0
    for item in items:
            if item.amount > 1:
                total += item.amount * item.dish.price
            else:
                total += item.dish.price
                
    return total

#if username exists func
def offer_name(request,username):
    users_queryset = User.objects.filter(username=username)
    while users_queryset.exists():
        username = (request.POST['first_name']) + str(random.randint(1,1000))
        users_queryset = User.objects.filter(username=username)
    
    return username