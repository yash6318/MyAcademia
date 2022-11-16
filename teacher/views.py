from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Teachers,TeacherDetails,Classes,Students,Attendance,Results
# Create your views here.

@login_required
def home(request):
    teach_name = request.user.get_full_name()
    curr_teacher = Teachers.objects.get(firstname=request.user.username)
    curr_teach_details = TeacherDetails.objects.get(teacherid=curr_teacher.teacherid)
    teaches_class = Classes.objects.get(classteacherid=curr_teacher.teacherid).class_field
    context ={
        'teach_name': teach_name,
        'curr_teach': curr_teacher,
        'curr_teach_details': curr_teach_details,
        'teach_class': teaches_class,
    }
    
    return render(request, 'teacher/teacher-home.html',context)

def my_class(request):
    curr_teacher = Teachers.objects.get(firstname=request.user.username)
    teaches_class = Classes.objects.get(classteacherid=curr_teacher.teacherid).class_field
    all_studs = Students.objects.filter(class_field=teaches_class)

    context={
        'all_studs':all_studs,
    }
    return render(request, 'teacher/teach_class.html',context)

def attendance(request):
    if request.method == 'POST':
        
        enrollno= request.POST.get('enrollno')
        month = request.POST.get('month')
        attendance = request.POST.get('attendance')

        stud = Attendance.objects.get(enrollno=enrollno)
        if month=='january':  stud.january = attendance
        elif month=='february':  stud.february = attendance
        elif month=='march':  stud.march = attendance
        elif month=='april':  stud.april = attendance
        elif month=='may':  stud.may = attendance
        elif month=='june':  stud.june = attendance
        elif month=='july':  stud.july = attendance
        elif month=='august':  stud.august = attendance
        elif month=='september':  stud.september = attendance
        elif month=='october':  stud.october = attendance
        elif month=='november':  stud.november = attendance
        elif month=='december':  stud.december = attendance

        stud.save()

        
    curr_teacher = Teachers.objects.get(firstname=request.user.username)
    teaches_class = Classes.objects.get(classteacherid=curr_teacher.teacherid).class_field
    all_studs = Students.objects.filter(class_field=teaches_class)
    attendance_of_stud = Attendance.objects.filter(class_field=teaches_class)
    zipped_list = zip(all_studs,attendance_of_stud)
    context={
        'ziplist':zipped_list,
    }
    return render(request, 'teacher/teach_att.html',context)

def marks(request):
    if request.method == 'POST':
        
        enrollno = request.POST.get('enrollno')
        sub = request.POST.get('sub')
        new_marks = request.POST.get('new_marks')
        
        studd = Results.objects.get(enrollno=enrollno)

        if sub=='sub1':  studd.marksinsub1 = new_marks
        elif sub=='sub2':  studd.marksinsub2 = new_marks
        elif sub=='sub3':  studd.marksinsub3 = new_marks
        elif sub=='sub4':  studd.marksinsub4 = new_marks
        elif sub=='sub5':  studd.marksinsub5 = new_marks
        elif sub=='sub6':  studd.marksinsub6 = new_marks
        elif sub=='sub7':  studd.marksinsub7 = new_marks
        # print(studd)
        studd.save()

    curr_teacher = Teachers.objects.get(firstname=request.user.username)
    teach_class = Classes.objects.get(classteacherid=curr_teacher.teacherid)
    teaches_class = teach_class.class_field
    all_studs = Students.objects.filter(class_field=teaches_class)
    marks_of_stud = Results.objects.filter(class_field=teaches_class)
    
    sub1 = teach_class.subject1
    sub2 = teach_class.subject2
    sub3 = teach_class.subject3
    sub4 = teach_class.subject4
    sub5 = teach_class.subject5
    sub6 = teach_class.subject6
    sub7 = teach_class.subject7

    zipped_list = zip(all_studs,marks_of_stud)
    context={
        'ziplist':zipped_list,
        'sub1' : sub1,
        'sub2' : sub2,
        'sub3' : sub3,
        'sub4' : sub4,
        'sub5' : sub5,
        'sub6' : sub6,
        'sub7' : sub7,
    }
    return render(request, 'teacher/teach_marks.html',context)
