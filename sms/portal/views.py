from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def showIndexPage(request):
    return render(request, "index.html")

def showLoginPage(request):
    return render(request, "login.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("Method not Allowed")

    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == "1":  # Admin
                return HttpResponseRedirect("/admin_home")
            elif user.user_type == "2":  # Teacher
                return HttpResponseRedirect("/staff_home")
            elif user.user_type == "3":  # Student
                return HttpResponseRedirect("/student_home")
            else:
                return HttpResponse("Invalid user type")
        else:
            messages.error(request,"Invalid Login")
            return HttpResponseRedirect("/")

def getUserDetails(request):
    if request.user!=None:
        return HttpResponse("User: " + request.user.username + "usertype: " + request.user.user_type)
    else:
        return HttpResponse("Please Login!")

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")
