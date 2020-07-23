from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User #added manually
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import time

from datetime import datetime
# Create your views here.

def LoginUser(request):
    print("running User")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username= username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/")
            # Redirect to a success page.
        else:
            return render(request, "login.html")
            
    return render(request, "login.html")
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
        print("redirected to /login")
    return render(request, "index.html")
def LogoutUser(request):
    logout(request)
    return redirect("/login")

def SignupUser(request):
    if request.method == "POST":
        create_username = request.POST.get("signup-username")
        password = request.POST.get("signup-password")
        cnf_password = request.POST.get("cnf-password")
        if password == cnf_password:
            try:
                new_user = User.objects.create_user(username=create_username, email=None, password=password)
                new_user.save()
                messages.success(request, 'You have Successfully Signed up')
            except:
                pass
        else:
            return render(request, "signup.html")
    return render(request, "signup.html")





def ChangePassword(request):
    if request.method == "POST":
        chk_username = request.POST.get("restoring-username")
        new_password = request.POST.get("new-pswd")
        cnf_new_password = request.POST.get("cnf-new-pswd")
        if new_password == cnf_new_password:
            try:
                u = User.objects.get(username=chk_username)
                u.set_password(cnf_new_password)
                u.save()
                messages.success(request, 'Your Password has been updated. You can login now !!')
            except Exception as e:
                return render(request, "change_pswd.html")
                messages.warning(request, 'Username is does not exists. Try reloading the page or look for a solution.')
            
        else:
            return render(request, "change_pswd.html")
            messages.warning(request, 'Password does\'nt match. Try again')
            
    return render(request, "change_pswd.html")
# python manage.py runserver
# python manage.py makemigrations
# python manage.py migrate
# python manage.py startapp
