from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from portal.models import CustomUser, Student, Subjects, Attendance, Teacher


def staffHome(request):
    teacher = Teacher.objects.get(user=request.user)
    # Get subjects assigned to this teacher
    subject_list = Subjects.objects.filter(teacher_id=teacher)

    context = {
        "teacher": teacher,
        "subject_list": subject_list
    }
    return render(request, "staff_template/staff_home.html", context)
    # return render(request, "staff_template/staff_home.html")

def takeAttendance(request):
    students = Student.objects.all()
    subjects = Subjects.objects.all()
    context = {
        "students": students,
        "subjects": subjects
    }
    return render(request, "staff_template/take_attendance.html", context)


def saveAttendance(request):
    if request.method != 'POST':
        messages.error(request, "Invalid request method")
        return HttpResponseRedirect("/take_attendance")

    student_id = request.POST.get("student_id")
    subject_id = request.POST.get("subject_id")
    date = request.POST.get("date")
    status = request.POST.get("status")

    try:
        student = Student.objects.get(id=student_id)
        subject = Subjects.objects.get(id=subject_id)

        # Check if record already exists for the same (student, subject, date)
        if Attendance.objects.filter(student=student, subject=subject, date=date).exists():
            messages.error(request, "Attendance already recorded for this student on this date.")
            return HttpResponseRedirect("/take_attendance")

        Attendance.objects.create(
            student=student,
            subject=subject,
            date=date,
            status=status
        )

        messages.success(request, "Attendance recorded successfully!")
        return HttpResponseRedirect("/take_attendance")

    except Student.DoesNotExist:
        messages.error(request, "Selected student does not exist.")
    except Subjects.DoesNotExist:
        messages.error(request, "Selected subject does not exist.")
    except Exception as e:
        print("Exception:", e)
        messages.error(request, "Something went wrong. Please try again.")

    return HttpResponseRedirect("/take_attendance")