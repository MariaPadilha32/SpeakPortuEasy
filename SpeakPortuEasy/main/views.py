from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
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

def query_class(request):
    return render(request, 'query-class.html')

def query_classroom(request):
    return render(request, 'query-classroom.html')

def query_enrollments(request):
    return render(request, 'query-enrollments.html')

def query_parents(request):
    return render(request, 'query-parents.html')

def query_profiles(request):
    return render(request, 'query-profiles.html')

def query_schedule(request):
    return render(request, 'query-schedule.html')

def query_student(request):
    return render(request, 'query-student.html')

def query_users(request):
    return render(request, 'query-users.html')

def query_zipcode(request):
    return render(request, 'query-zipcode.html')

def delete_student(request):
    return render(request, 'delete-student.html')

def delete_class(request):
    return render(request, 'delete-class.html')

def delete_schedule(request):
    return render(request, 'delete-schedule.html')

def delete_classroom(request):
    return render(request, 'delete-classroom.html')

def delete_enrollments(request):
    return render(request, 'delete-enrollments.html')

def delete_users(request):
    return render(request, 'delete-users.html')

def delete_profiles(request):
    return render(request, 'delete-profiles.html')

def delete_parents(request):
    return render(request, 'delete-parents.html')

def delete_zipcode(request):
    return render(request, 'delete-zipcode.html')

def edit_student(request):
    return render(request, 'edit-student.html')

def edit_class(request):
    return render(request, 'edit-class.html')

def edit_schedule(request):
    return render(request, 'edit-schedule.html')

def edit_classroom(request):
    return render(request, 'edit-classroom.html')

def edit_enrollments(request):
    return render(request, 'edit-classroom.html')

def edit_users(request):
    return render(request, 'edit-users.html')

def edit_profiles(request):
    return render(request, 'edit-profiles.html')

def edit_parents(request):
    return render(request, 'edit-parents.html')

def edit_zipcode(request):
    return render(request, 'edit-zipcode.html')