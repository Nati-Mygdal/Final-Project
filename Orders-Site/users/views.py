from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User
from utils import offer_name
# Create your views here.

# main pages

def main(request):
    return render(request,'main/main_page.html')

def about_us(request):
    return render(request,'main/about.html')

# user handling

def user_login(request):
    if request.method == 'POST':
        user = authenticate(request,
                            username=request.POST['username'],
                            password=request.POST['password']
                            )
        if user is not None:
            if user.is_staff:
                messages.error(request,f"Hello {user.username}! you have been redirected to managers-login page, please log in again.")
                return redirect('manager-login')
            else:
                login(request,user)
                messages.success(request,'Logged in!')
                return redirect('main-page')
        elif User.objects.filter(username=request.POST['username']).exists():
            messages.error(request,'Wrong password.')
            return redirect('user-login')
        else:
            messages.error(request,'no username with this name found.')
            return redirect('user-login')
    return render(request,'users/login.html')

def signup(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])
            name_offer = offer_name(request,request.POST['username'])
            messages.error(request,f'username allready in use. you can try {name_offer}.')
            return redirect('user-signup')
        except:
            user = None
        if not user:
            try:
                user = User.objects.get(email=request.POST['email'])
                messages.error(request,'email allready in use.')
                return redirect('user-signup')
            except:
                user = None
            if not user:
                if request.POST['confirm_password'] == request.POST['password']:
                    if (request.POST['first_name']).isalpha() and (request.POST['last_name']).isalpha():
                        if not (request.POST['username']).isdigit():
                            new_user = User(
                                username = request.POST['username'],
                                password = make_password(request.POST['password']),
                                first_name = request.POST['first_name'],
                                last_name = request.POST['last_name'],
                                email = request.POST['email'],
                            )
                            new_user.save()
                            messages.success(request,'Success, User created. Please login to start ordering.')
                            return redirect('main-page')
                        else:
                            messages.error(request,'username cant contain numbers only.')
                    else:
                        messages.error(request,'Cant use numbers in first and last name.')
                else:
                    messages.error(request,'Passwords did not match. Signup failed.')
    return render(request,'users/signup.html')

@login_required(login_url='user-login')
def user_logout(request):
    logout(request)
    return redirect('main-page')