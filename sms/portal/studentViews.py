from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from portal.models import Student, Subjects, Attendance

def studentHome(request):
    student = Student.objects.get(user=request.user)
    subject_data = Subjects.objects.filter(program_id=student.program_id)

    subject_attendance = []

    for subject in subject_data:
        present_count = Attendance.objects.filter(student=student, subject=subject, status="Present").count()
        absent_count = Attendance.objects.filter(student=student, subject=subject, status="Absent").count()
        
        subject_attendance.append({
            'subject_name': subject.subject_name,
            'program_name': subject.program_id.program_name,
            'present': present_count,
            'absent': absent_count,
        })

    context = {
        'student': student,
        'subject_attendance': subject_attendance
    }
    return render(request, 'student_template/student_home.html', context)
