from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Blog
# Create your views here.
def home(request):
    blog = Blog.objects.all()
    return render(request,'home.html',{'blog':blog})

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        if pass1 != pass2:
            messages.warning(request,'Password not match')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'Email already Exist')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.warning(request,'Username already Exist')
            return redirect('register')
        else:
            print(firstname,lastname,email,username,pass1,pass2)
            # user = User(first_name=firstname,last_name=lastname,email=email,username=username,password = pass2)
            user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=pass1)
            user.save()
            messages.success(request,'New User Created')
            return redirect('login')
    return render(request,'login.html')
    
def loginFun(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        # uname = request.POST['username']
        # passw = request.POST['password']
        u = authenticate(username=uname,password=passw)
        if u is not None:
            login(request,u)
            return redirect('home')
        else:
            messages.warning(request,'Invalid Credentials')
            return redirect('login')
    return redirect('login')

def logoutFun(request):
    logout(request)
    return redirect('home')







# pratiksha@gmail.com , pratiksha
# superuser superuser

# normal users
