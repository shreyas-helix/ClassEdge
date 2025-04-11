from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Teacher, Student, Subjects, Admin, Program, Attendance, CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subjects)
admin.site.register(Admin)
admin.site.register(Program)
admin.site.register(Attendance)