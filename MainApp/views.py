from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from MainApp.models import Applicants

# Create your views here.
def home(request):
    return render (request, 'MainApp/home.html')

def my_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            if user.groups.filter(name='Student'):
                messages.success(request, 'Successfully logged in!')
                return redirect('stud-home')
            elif user.groups.filter(name='Teacher'):
                messages.success(request, 'Successfully logged in!')
                return redirect('teacher-home')
            else:
                messages.error(request,'Something went wrong! Please try again')
                return redirect('login')
        else:
            messages.error(request,'Username or Password is incorrect!')
            return redirect('login')
    else:
        return redirect('login')

def application_view(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        classtobeenrolled = request.POST.get('classtobeenrolled')
        lastschoolattended = request.POST.get('lastschoolattended')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        bloodgrp = request.POST.get('bloodgrp')
        aadhaarno = request.POST.get('aadhaarno')
        contactno = request.POST.get('contactno')
        father_s_name = request.POST.get('fathername')
        father_s_occupation = request.POST.get('fatherocc')
        father_s_aadhaarno = request.POST.get('fatheraadhaar') or None  # Set to None if empty
        father_s_email = request.POST.get('fatheremail') or None  # Set to None if empty
        father_s_contactno = request.POST.get('fathercontact') or None  # Set to None if empty
        mother_s_name = request.POST.get('mothername')
        mother_s_occupation = request.POST.get('motherocc')
        mother_s_aadhaarno = request.POST.get('motheraadhaar') or None  # Set to None if empty
        mother_s_email = request.POST.get('motheremail') or None  # Set to None if empty
        mother_s_contactno = request.POST.get('mothercontact') or None  # Set to None if empty
        guardian_s_name = request.POST.get('guardianname')
        guardian_s_occupation = request.POST.get('guardianocc')
        guardian_s_aadhaarno = request.POST.get('guardianaadhaar') or None  # Set to None if empty
        guardian_s_email = request.POST.get('guardianemail') or None  # Set to None if empty
        guardian_s_contactno = request.POST.get('guardiancontact') or None  # Set to None if empty
        familyincome = request.POST.get('familyincome') or None  # Set to None if empty
        caste = request.POST.get('caste') or None  # Set to None if empty
        religion = request.POST.get('religion') or None  # Set to None if empty

        applicant = Applicants(
            firstname=firstname,
            lastname=lastname,
            classtobeenrolled=classtobeenrolled,
            lastschoolattended=lastschoolattended,
            gender=gender,
            dob=dob,
            address=address,
            bloodgrp=bloodgrp,
            aadhaarno=aadhaarno,
            contactno=contactno,
            father_s_name=father_s_name,
            father_s_occupation=father_s_occupation,
            father_s_aadhaarno=father_s_aadhaarno,
            father_s_email=father_s_email,
            father_s_contactno=father_s_contactno,
            mother_s_name=mother_s_name,
            mother_s_occupation=mother_s_occupation,
            mother_s_aadhaarno=mother_s_aadhaarno,
            mother_s_email=mother_s_email,
            mother_s_contactno=mother_s_contactno,
            guardian_s_name=guardian_s_name,
            guardian_s_occupation=guardian_s_occupation,
            guardian_s_aadhaarno=guardian_s_aadhaarno,
            guardian_s_email=guardian_s_email,
            guardian_s_contactno=guardian_s_contactno,
            familyincome=familyincome,
            caste=caste,
            religion=religion,
        )

        applicant.save()

    return render(request, 'MainApp/application.html')


def prospectus(request):
    return render(request, 'MainApp/prospectus.html')

def terms(request):
    return render(request, 'MainApp/terms.html')

