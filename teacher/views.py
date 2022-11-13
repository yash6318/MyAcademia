from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required
def home(request):
    teach_name = request.user.get_full_name()

    context ={
        'teacher_name': teach_name,
    }
    return render(request, 'teacher/teacher-home.html',context)

def my_class(request):
    return render(request, 'teacher/teach_class.html')

def attendance(request):
    return render(request, 'teacher/teach_att.html')

def marks(request):
    return render(request, 'teacher/teach_marks.html')
