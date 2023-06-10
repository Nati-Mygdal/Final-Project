from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    imageUrl = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Dish(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    imageUrl = models.TextField()
    is_gluten_free = models.BooleanField(default=False)
    is_vegeterian = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    dish = models.ForeignKey(Dish,on_delete=models.CASCADE)
    cart = models.ForeignKey('orders.Cart',on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

