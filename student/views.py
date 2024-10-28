from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from MainApp.models import Students,StudentDetails,Attendance,Results,Classes,Subjects
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
    context = {
        'res': curr_stud_res,
        'stud_class':stud_class,
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

    sub1_info = Subjects.objects.get(subjectcode = sub1).subjectname
    sub2_info = Subjects.objects.get(subjectcode = sub2).subjectname
    sub3_info = Subjects.objects.get(subjectcode = sub3).subjectname
    sub4_info = Subjects.objects.get(subjectcode = sub4).subjectname
    sub5_info = Subjects.objects.get(subjectcode = sub5).subjectname if sub5 else None
    sub6_info = Subjects.objects.get(subjectcode = sub6).subjectname if sub6 else None
    sub7_info = Subjects.objects.get(subjectcode = sub7).subjectname if sub7 else None

    context = {
        'stud_class':stud_class,
        'sub1' : sub1,
        'sub1_info': sub1_info,
        'sub2' : sub2,
        'sub2_info': sub2_info,
        'sub3' : sub3,
        'sub3_info': sub3_info,
        'sub4' : sub4,
        'sub4_info': sub4_info,
        'sub5' : sub5,
        'sub5_info': sub5_info,
        'sub6' : sub6,
        'sub6_info': sub6_info,
        'sub7' : sub7,
        'sub7_info': sub7_info,
    }
    return render(request,'student/stud_subjects.html',context)