from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'base.html')
    #return HttpResponse('Hello World - Welcome to Django Framework')

def register_student(request):
    return render(request, 'register-student.html')

def register_class(request):
    return render(request, 'register-class.html')

def register_schedule(request):
    return render(request, 'register-schedule.html')

def register_classroom(request):
    return render(request, 'register-classroom.html')

def register_enrollments(request):
    return render(request, 'register-classroom.html')

def register_users(request):
    return render(request, 'register-users.html')

def register_profiles(request):
    return render(request, 'register-profiles.html')

def register_parents(request):
    return render(request, 'register-parents.html')

def register_zipcode(request):
    return render(request, 'register-zipcode.html')