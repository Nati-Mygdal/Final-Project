from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='main-page'),
    path('about/',views.about_us,name='about-us'),
    path('login/',views.user_login,name='user-login'),
    path('signup/',views.signup,name='user-signup'),
    path('logout/',views.user_logout,name='user-logout')
]