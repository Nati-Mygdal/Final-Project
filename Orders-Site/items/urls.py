from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/',views.show_dishes,name='show-dishes'),
    path('dishes/',views.show_dish_order,name='dishes-by-order'),
    path('cat/',views.show_categories,name='show-categories')
]