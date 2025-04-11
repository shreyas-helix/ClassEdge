"""
URL configuration for student_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from student_platform import settings
from portal import adminViews, staffViews, studentViews
from portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showLoginPage),
    path('index/', views.showIndexPage),
    path('doLogin', views.doLogin),
    path('get_user_details', views.getUserDetails),
    path('logout_user', views.logoutUser),
    path('admin_home', adminViews.adminHome),
    path('add_staff', adminViews.addStaff),
    path('save_staff', adminViews.saveStaff),
    path('add_student',adminViews.addStudent),
    path('save_student', adminViews.saveStudent),
    path('add_program', adminViews.addProgram),
    path('save_program', adminViews.saveProgram),
    path('manage_staff', adminViews.manageStaff),
    path('manage_student',adminViews.manageStudent),
    path('add_subject', adminViews.addSubject),
    path('save_subject',adminViews.saveSubject),
    path('staff_home', staffViews.staffHome),
    path('student_home',studentViews.studentHome),
    path('take_attendance', staffViews.takeAttendance),
    path('save_attendance', staffViews.saveAttendance),
    path('view_attendance', adminViews.viewAttendance),
    

    ]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
