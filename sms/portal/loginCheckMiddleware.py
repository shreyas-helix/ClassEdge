from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect


class LoginCheckMiddleWare(MiddlewareMixin):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        # print(modulename)
        user = request.user

        #Check whether the user is logged in or not
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "portal.adminViews":
                    pass
                elif modulename == "portal.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect("/admin_home")
            
            elif user.user_type == "2":
                if modulename == "portal.staffViews":
                    pass
                elif modulename == "portal.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect("/staff_home")
            
            elif user.user_type == "3":
                if modulename == "portal.studentViews":
                    pass
                elif modulename == "portal.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect("/student_home")

            else:
                return HttpResponseRedirect("/")

        else:
            if request.path == reverse("login") or request.path == reverse("doLogin"):
                pass
            else:
                return HttpResponseRedirect("/")