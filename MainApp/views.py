from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
                messages.error(request,'Username or Password is incorrect!')
                return redirect('login')
        # else:
        #     # Return an 'invalid login' error message.
        #     ...
    else:
        return redirect('login')