from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.

class LoginView(View):
    def get(self,request):
        return render(request,'accounts/login.html')
    
    def post(self,request):
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"login successful")
            return redirect('dashboard')
        messages.error(request,'login failed')
        return redirect('login')



class DashboardView(View):
    def get(self,request):
      if not request.user.is_authenticated:
          messages.error(request,'unauthorized access')
          return redirect('login')
      return render(request,'dashboard.html')
    

class RegistrationView(View):
    def get(self,request):
        return render(request,'accounts/registration.html')
    
    def post(self,request):
        first_name =  request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email= request.POST.get('email')
        username = request.POST.get('username')
        password= request.POST.get('password')
        try:

            user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            if user is not None: #this line of code will check whether user is created or not
                user.is_active=True
                user.save()
                send_mail(
                    'Account creation',
                    'Your account has been created successfully. Welcome to SES',
                    settings.EMAIL_HOST_USER, 
                    [user.email] #receiver email address

                )
                messages.success(request,'Registered successfully')
                return redirect('login')
            messages.error(request,"something went wrong")
            return redirect('register')
        except:
            messages.error(request,'something went wrong')
            return redirect('register')
        



class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')
