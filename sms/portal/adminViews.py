from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import datetime

 

from portal.models import CustomUser, Teacher, Program, Subjects, Attendance

def adminHome(request):
    return render(request,"admin_template/admin_home.html")

def addStaff(request):
    return render(request, "admin_template/add_staff.html")

def saveStaff(request):
    if request.method != 'POST':
        messages.error(request, "Invalid method")
        return HttpResponseRedirect("/add_staff")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        teacher_type = 2
        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=teacher_type)
            user.teacher.address = address
            user.save()
           
            messages.success(request, "Successfully Added!")
            return HttpResponseRedirect('/add_staff')
        except Exception as e:
            print("Exception:", e)
            messages.error(request, "Failed to Add :(")
            return HttpResponseRedirect('/add_staff')

def addProgram(request):
    return render(request, "admin_template/add_program.html")

def saveProgram(request):
    if request.method != 'POST':
        messages.error(request, "Invalid method")
        return HttpResponseRedirect("/add_program")
    else:
        program = request.POST.get("program_name")
        try:
            new_program_model = Program(program_name = program)
            new_program_model.save()
            messages.success(request, "Program Added Successfully!")
            return HttpResponseRedirect('/add_program')
        except:
            messages.error(request, 'Failed to add program, try again!')
            return HttpResponseRedirect('/add_program')

def addStudent(request):
    programs = Program.objects.all()
    context = {
        "programs":programs
    }
    return render(request, "admin_template/add_student.html", context)

def saveStudent(request):
        if request.method != 'POST':
            messages.error(request, "Invalid method")
            return HttpResponseRedirect("/add_student")
        else:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            address = request.POST.get("address")
            dob = request.POST.get("dob")
            phone_number = request.POST.get("phone_number")
            program_id = request.POST.get("program")
            gender = request.POST.get("gender")
            student_type = 3
            try:
                user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=student_type)
                user.student.address = address
                user.student.date_of_birth = dob
                user.student.phone_number = phone_number
                user.student.gender = gender
                program_obj = Program.objects.get(id=program_id)
                user.student.program_id = program_obj
                user.save()
            
                messages.success(request, "Successfully Added!")
                return HttpResponseRedirect('/add_student')
            except Exception as e:
                print("Exception:", e)
                messages.error(request, "Failed to Add :(")
                return HttpResponseRedirect('/add_student')


def addSubject(request):
    programs = Program.objects.all()
    teachers = Teacher.objects.all()
    context = {
        "programs" : programs,
        "teachers" : teachers
    }
    return render(request, "admin_template/add_subject.html", context)

def saveSubject(request):
    if request.method != 'POST':
        messages.error(request, "Invalid method")
        return HttpResponseRedirect("/add_subject")
    else:
        subject_name = request.POST.get("subject_name")
        program_id = request.POST.get('program')
        program = Program.objects.get(id=program_id)
        
        teacher_id = request.POST.get('teacher')
        teacher = Teacher.objects.get(id=teacher_id)
        try:
            subject = Subjects(subject_name=subject_name,program_id=program, teacher_id=teacher)
            subject.save()
            messages.success(request, "Program Added Successfully!")
            return HttpResponseRedirect('/add_subject')
        except:
            messages.error(request, 'Failed to add subject, try again!')
            return HttpResponseRedirect('/add_subject')
        

def viewAttendance(request):
    attendance_records = Attendance.objects.select_related('student__user', 'subject').order_by('-date')
    context = {
        "attendance_records": attendance_records
    }
    return render(request, "admin_template/view_attendance.html", context)


def manageStaff(request):
    return render(request, "admin_template/manage_staff.html")

def manageStudent(request):
    return render(request, "admin_template/manage_student.html")