from django.db import models
from users.models import User
from items.models import Dish
# Create your models here.

class Cart(models.Model):
    profile_id = models.ForeignKey(User,on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish, through='items.Item')
    is_done = models.BooleanField(default=False)

class Delivery(models.Model):
    is_delivered = models.BooleanField(default=False)
    address = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    phone = models.CharField(max_length=10,default='')
    created = models.DateTimeField(auto_now_add=True)
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE,primary_key=True)



