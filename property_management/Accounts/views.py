from django.shortcuts import render,redirect
from . models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def sign_up(request):
    user=None
    error_msg=None
    if request.POST:
        username = request.POST.get('username')
        full_name = request.POST.get('fullname')
        email = request.POST.get('email')
        ph_no = request.POST.get('ph_no')
        address = request.POST.get('address')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(
                username=username,
                full_name=full_name,
                email=email,
                password=password,
                ph_no=ph_no,
                address=address
            )
            return redirect('Login')
        except Exception:
            error_msg="Username Already Exists"
    return render(request,'Sign_Up.html',{'user':user,'Error_Message':error_msg})

def Login(request):
    error_msg=None
    if request.POST:
        uname=request.POST.get("username")
        passwd=request.POST.get("password")
        user=authenticate(username=uname,password=passwd)
        if user:
            if user.role == 'company_admin':
                login(request,user)
                return redirect('Company Home')
            elif user.role == 'tenant':
                login(request,user)
                return redirect('User Property List')
        else:
            error_msg="Invalid Credentials"
    return render(request,'Login.html',{'Error_Message':error_msg})

def Logout(request):
    logout(request)
    return redirect('Home Page')

def delete_account(request):
    user=request.user
    user.delete()
    return redirect('Home Page')