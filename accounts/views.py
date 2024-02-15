from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(email = username).exists():
            messages.info(request,'User doesn\'t exists with these user name')
            return redirect('login')
        user = authenticate(email = username, password = password)
        if user is None:
            messages.info(request, 'Incorrect password')
            return redirect('login')
        else:
            login(request, user)
            return redirect('home')

    return render(request, 'login/login.html')


def signupPage(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        phone = request.POST.get('uphone')
        password = request.POST.get('upassword')
        confPassword = request.POST.get('confpassword')

        if not password == confPassword:
            messages.info(request, 'Password doesn\'t match')
        if User.objects.filter(email = email).exists():
            messages.info(request, 'User already exists with this email id')
            return redirect('signup')
        else:
            user = User.objects.create(
                name = name,
                email = email,
                phone = phone,
            )
            user.set_password(password)
            user.save()
            messages.success(request, "Account has been created successfully")
            login(request, user)
            return redirect('home')
    return render(request, 'signup/signup.html')


def logoutPage(request):
    logout(request)
    return redirect('home')




def adminLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(email = username).exists():
            return redirect('adminlogin')
        user = authenticate(email = username, password = password)
        if user is None:
            messages.info(request, 'Incorrect password')
            return redirect('adminlogin')
        else:
            if user.is_superuser:
                login(request, user)
                return redirect('dashboard')
            else:
                return redirect('login')
    return render(request, 'adminlogin/adminlogin.html')