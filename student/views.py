from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required
def home(request):
    stud_name = request.user.get_full_name()

    context ={
        'Student_name': stud_name,
    }
    return render(request, 'student/student-home.html',context)

def attendance(request):
    return render(request, 'student/stud_attendance.html')

def marks(request):
    return render(request, 'student/stud_marks.html')