from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Students,StudentDetails,Attendance,Results,Classes
# Create your views here.

@login_required
def home(request):
    stud_name = request.user.get_full_name()
    curr_stud = Students.objects.get(firstname=request.user.username)
    curr_stud_details = StudentDetails.objects.get(enrollno=curr_stud.enrollno)
    context ={
        'Student_name': stud_name,
        'curr_stud': curr_stud,
        'curr_stud_details': curr_stud_details,
    }
    return render(request, 'student/student-home.html',context)

def attendance(request):
    curr_stud = Students.objects.get(firstname=request.user.username)
    curr_stud_att = Attendance.objects.get(enrollno=curr_stud.enrollno)
    # print(curr_stud_att)
    return render(request, 'student/stud_attendance.html',{'att':curr_stud_att})

def marks(request):
    curr_stud = Students.objects.get(firstname=request.user.username)
    curr_stud_res = Results.objects.get(enrollno=curr_stud.enrollno)
    stud_class= Classes.objects.get(class_field= curr_stud.class_field)
    sub1 = stud_class.subject1
    sub2 = stud_class.subject2
    sub3 = stud_class.subject3
    sub4 = stud_class.subject4
    sub5 = stud_class.subject5
    sub6 = stud_class.subject6
    sub7 = stud_class.subject7
    context = {
        'res': curr_stud_res,
        'stud_class':stud_class,
        'sub1' : sub1,
        'sub2' : sub2,
        'sub3' : sub3,
        'sub4' : sub4,
        'sub5' : sub5,
        'sub6' : sub6,
        'sub7' : sub7,
    }
    return render(request, 'student/stud_marks.html',context)

def subj(request):
    curr_stud = Students.objects.get(firstname=request.user.username)
    stud_class= Classes.objects.get(class_field= curr_stud.class_field)
    sub1 = stud_class.subject1
    sub2 = stud_class.subject2
    sub3 = stud_class.subject3
    sub4 = stud_class.subject4
    sub5 = stud_class.subject5
    sub6 = stud_class.subject6
    sub7 = stud_class.subject7

    context = {
        'stud_class':stud_class,
        'sub1' : sub1,
        'sub2' : sub2,
        'sub3' : sub3,
        'sub4' : sub4,
        'sub5' : sub5,
        'sub6' : sub6,
        'sub7' : sub7,
    }
    return render(request,'student/stud_subjects.html',context)