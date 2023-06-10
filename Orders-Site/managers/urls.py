from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.manager_login,name='manager-login'),
    path('users/',views.manage_users,name='manage-users'),
    path('edit/user/<int:id>',views.edit_user,name='edit-user'),
    path('makemanager/<int:id>',views.make_manager,name='make-manager'),
    path('cancelmanager/<int:id>',views.cancel_manager,name='cancel-manager'),
    path('delete/user/<int:id>',views.delete_user,name='delete-user'),
    path('categories/',views.manage_categories,name='manage-categories'),
    path('cat/<int:id>',views.manage_category,name='manage-category'),
    path('cat/<int:id>/del/',views.delete_cat,name='delete-category'),
    path('cat/add/',views.add_category,name='add-category'),
    path('dishes/',views.manage_dishes,name='manage-dishes'),
    path('cat/<int:id>/dishes',views.manage_dishes_by_cat,name='manage-dish-by-cat'),
    path('dish/<int:id>/edit/',views.manage_dish,name='manage-dish'),
    path('dish/<int:id>/delete/',views.delete_dish,name='delete-dish'),
    path('dish/add/',views.add_dish,name='add-dish'),
    path('deliveries/',views.manage_deliveries,name='manage-deliveries'),
    path('deliveries/byid',views.delivery_by_id,name='delivery-by-id'),
    path('delivery/del/<int:id>',views.delete_delivery,name='delete-del'),
    path('delivery/check/<int:id>',views.check_arrived,name='mark-arrived'),
    path('delivery/uncheck/<int:id>',views.mark_unarrived,name='mark-unarrived'),
    path('deliveries/byarrived/',views.delivery_by_arrived,name='by-arrived'),
    path('deliveries/bynotarrived',views.delivery_by_not_arrived,name='by-not-arrived'),
    path('carts/',views.manage_carts,name='manage-carts'),
    path('carts/byuserid/',views.carts_by_user_id,name='carts-by-user-id'),
    path('carts/byusername/',views.carts_by_username,name='carts-by-username'),
    path('cart/byid/',views.cart_by_id,name='cart-by-id'),
    path('carts/delete/<int:id>/',views.delete_cart,name='delete-cart'),
]