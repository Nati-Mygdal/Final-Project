from django.urls import path
from . import views

urlpatterns = [
    path('cart/<int:id>/',views.show_cart,name='show-cart'),
    path('history/<int:id>/',views.history,name='order-history'),
    path('info/<int:id>/',views.information,name='order-info'),
    path('add/<int:id>/',views.add_to_cart,name='add-to-cart'),
    path('delete/<int:id>/',views.delete_from_cart,name='delete-dish-from-cart'),
    path('reorder/<int:id>/',views.re_order,name='re-order')
]