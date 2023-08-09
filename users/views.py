from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerUser(request):
    if request.method == "POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmpassword")
        print(username,email,firstname,lastname,password,confirmpassword)

        if password==confirmpassword:
            users = User.objects.create_user(
                username=username,
                first_name=firstname,
                last_name=lastname,
                email=email,
                password=password

        )
        users.save()
        return redirect("migrations:index")
       
    return render(request,"users/register.html")

def loginUser(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("migrations:index")
        context = {
            "error":"Invalid Credentials"
        }
        return redirect("users:login")
    return render(request,"users/login.html")

@login_required
def logoutUser(request):
    logout(request)
    return redirect("migrations:index")