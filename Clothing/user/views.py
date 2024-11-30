from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def sign_up(request):
    
    if request.method == 'POST' :
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.filter(username=username)

        print(fname,lname,username,password)
        
        if user is not None:
            messages.warning(request,'User already exists')

        
        else :
            user = User(username=username,first_name = fname , last_name = lname)
            user.set_password(password)
            user.save()
            
            return redirect('shop/')
    return render(request,'signup.html')
        
        
    
def log_in(request):
    
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.filter(username=username).exists()
        
      
        valid = authenticate(username=username,password=password)

        
        if not user:
            messages.warning(request,'User Doesnt exists')

        elif valid is None:
            messages.error(request,'Incorrect Password')
        else :
            
            login(request,valid)
            return redirect('/shop/')
    return render(request,'login.html')






    