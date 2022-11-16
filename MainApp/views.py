from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Applicants

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
        firstname = request.POST.firstname
        lastname = request.POST.lastname
        classtobeenrolled = request.POST.classtobeenrolled
        email = request.POST.email
        lastschoolattended = request.POST.lastschoolattended
        gender = request.POST.gender
        dob = request.POST.dob
        bloodgrp = request.POST.bloodgrp
        religion = request.POST.religion
        caste = request.POST.caste
        contactno = request.POST.contactno
        aadhaarno = request.POST.aadhaarno
        fathername = request.POST.fathername
        fatherocc = request.POST.fatherocc
        fatheremail = request.POST.fatheremail
        fathercontact = request.POST.fathercontact
        fatheraadhaarno = request.POST.fatheraadhaar
        mothername = request.POST.mothername
        motherocc = request.POST.motherocc
        motheremail = request.POST.motheremail
        mothercontact = request.POST.mothercontact
        motheraadhaarno = request.POST.motheraadhaar
        guardianname = request.POST.guardianname
        guardianemail = request.POST.guardianemail
        guardianocc = request.POST.guardianocc
        guardiancontact = request.POST.guardiancontact
        guardianaadhaar = request.POST.guardianaadhaar
        familyincome = request.POST.familyincome
        address = request.POST.address

        applicant = Applicants(
            firstname=firstname,
            lastname=lastname,
            classtobeenrolled=classtobeenrolled,
            email=email,
            lastschoolattended=lastschoolattended,
            gender=gender,
            dob=dob,
            bloodgrp=bloodgrp,
            religion=religion,
            caste=caste,
            contactno=contactno,
            aadhaarno=aadhaarno,
            father_s_name=fathername,
            father_s_occ=fatherocc,
            father_s_email=fatheremail,
            father_s_contact=fathercontact,
            father_s_aadhaarno=fatheraadhaarno,
            mother_s_name=mothername,
            mother_s_occ=motherocc,
            mother_s_email=motheremail,
            mother_s_contact=mothercontact,
            mother_s_aadhaarno=motheraadhaarno,
            guardian_s_name=guardianname,
            guardian_s_email=guardianemail,
            guardian_s_occ=guardianocc,
            guardian_s_contact=guardiancontact,
            guardian_s_aadhaar=guardianaadhaar,
            familyincome=familyincome,
            address=address,
        )

        applicant.save()
        
        


    return render(request, 'MainApp/application.html')

def prospectus(request):
    return render(request, 'MainApp/prospectus.html')

def terms(request):
    return render(request, 'MainApp/terms.html')

