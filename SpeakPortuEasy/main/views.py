from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from main.models import Classroom, Student, Enrollments, Classes, Schedule, Users, Profiles, Parents, Zipcodes
from .forms import ClassroomForm, StudentForm, EnrollmentsForm, ClassesForm, ScheduleForm, UsersForm, ProfilesForm, ParentsForm, ZipCodeForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('Hello World - Welcome to Django Framework')

@login_required(login_url='login')
def register_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        count = Student.objects.filter(name=name).count()
        if count > 0:
            messages.error(request, 'There is a student with that name, please use a different name.')
            return redirect('register-student')
        
        if request.method =='POST':
           form = StudentForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('query-student')
           else:
               return redirect('register-student')
    else:
        form = StudentForm()
        return render(request, 'register-student.html', {'form' : form})


@login_required(login_url='login')
def register_class(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        count = Classes.objects.filter(name=name).count()
        if count > 0:
            messages.error(request, 'There is a class with that name, please use a different name.')
            return redirect('register-class')
        if request.method =='POST':
           form = ClassesForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('query-class')
           else:
               return redirect('register-class')
    else:
        form = ClassesForm()
        return render(request, 'register-class.html', {'form' : form})

@login_required(login_url='login')
def register_schedule(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        count = Schedule.objects.filter(name=name).count()
        if count > 0:
            messages.error(request, 'There is no schedule available at that time, please try a different one.')
            return redirect('register-schedule')
        if request.method =='POST':
           form = ScheduleForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('query-schedule')
           else:
               return redirect('register-schedule')
    else:
        form = ScheduleForm()
        return render(request, 'register-schedule.html', {'form' : form})

@login_required(login_url='login')
def register_classroom(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        count = Classroom.objects.filter(name=name).count()
        if count > 0:
            messages.error(request,'There is a classroom with that name, please use a different name.')
            return redirect('register-classroom')
        if request.method == 'POST':
            form = ClassroomForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('query-classroom')
            else:
                return redirect('register-classroom')
    else:
        form = ClassroomForm()
        return render(request, 'register-classroom.html', {'form' : form})

@login_required(login_url='login')
def register_enrollments(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        count = Enrollments.objects.filter(name=name).count()
        if count > 0:
            messages.error(request, 'Please use a different name.')
            return redirect('register-enrollments')
        if request.method == 'POST':
            form = EnrollmentsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('query-enrollments')
            else:
                return redirect('register-enrollments')
    else:
        form = EnrollmentsForm()
        return render(request, 'register-enrollments.html', {'form' : form})

@login_required(login_url='login')
def register_users(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        count = Users.objects.filter(name=name).count()
        if count > 0:
            messages.error(request, 'This user information is not available, try a new one.')
            return redirect('register-users')
        if request.method == 'POST':
            form = UsersForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('query-users')
            else:
                return redirect('register-users')
    else:
        form = UsersForm()
        return render(request, 'register-users.html', {'form' : form})

@login_required(login_url='login')
def register_profiles(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        count = Profiles.objects.filter(name=name).count()
        if count > 0:
            messages.error(request, 'This profile has already been used, try a new one.')
            return redirect('register-profiles')
        if request.method == 'POST':
            form = ProfilesForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('query-profiles')
            else:
                return redirect('register-profiles')
    else:
        form = ProfilesForm()
        return render(request, 'register-profiles.html', {'form' : form})

@login_required(login_url='login')
def register_parents(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        count = Parents.objects.filter(name=name).count()
        if count > 0:
            messages.error(request, 'This name has been used')
            return redirect('register-parents')
        if request.method == 'POST':
            form = ParentsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('query-parents')
            else:
                return redirect('register-parents')
    else:
        form = ParentsForm()
        return render(request, 'register-parents.html', {'form' : form})

@login_required(login_url='login')
def register_zipcode(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        count = Zipcodes.objects.filter(name=name).count()
        if count > 0:
            messages.error(request, 'This Zipcode has been used')
            return redirect('register-zipcode')
        if request.method == 'POST':
            form = ZipcodeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('query-zipcode')
            else:
                return redirect('register-zipcode')
    else:
        form = ZipCodeForm()
        return render(request, 'register-ziocode.html', {'form' : form})

@login_required(login_url='login')
def query_class(request):
    form = ClassesForm
    classes = Classesroom.objects.all()
    total = Classes.objects.count()
    list_classes = Classes.objects.all()
    paginator = Paginator(list_classes, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'query-class.html', {'form' : form, 'classes': classes, 'total' : total, 'page_obj' : page_obj})

@login_required(login_url='login')
def query_classroom(request):
    form = ClassroomForm
    classrooms = Classroom.objects.all()
    total = Classroom.objects.count()
    list_classroom = Classroom.objects.all()
    paginator = Paginator(list_classroom, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'query-classroom.html', {'form' : form, 'classrooms': classrooms, 'total' : total, 'page_obj' : page_obj})

@login_required(login_url='login')
def query_enrollments(request):
    form = EnrollmentsForm
    enrollments = Enrollments.objects.all()
    total = Enrollments.objects.count()
    list_enrollment = Enrollments.objects.all()
    paginator = Paginator(list_enrollment, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'query-enrollments.html', {'form' : form, 'classrooms': classrooms, 'total' : total, 'page_obj' : page_obj})

@login_required(login_url='login')
def query_parents(request):
    return render(request, 'query-parents.html')

@login_required(login_url='login')
def query_profiles(request):
    return render(request, 'query-profiles.html')

@login_required(login_url='login')
def query_schedule(request):
    return render(request, 'query-schedule.html')

@login_required(login_url='login')
def query_student(request):
    return render(request, 'query-student.html')

@login_required(login_url='login')
def query_users(request):
    return render(request, 'query-users.html')

@login_required(login_url='login')
def query_zipcode(request):
    return render(request, 'query-zipcode.html')

@login_required(login_url='login')
def delete_student(request):
    return render(request, 'delete-student.html')

@login_required(login_url='login')
def delete_class(request):
    return render(request, 'delete-class.html')

@login_required(login_url='login')
def delete_schedule(request):
    return render(request, 'delete-schedule.html')

@login_required(login_url="accounts/login")
def delete_classroom(request, id):
    classroom = Classroom.objects.get(id=id)
    classroom.delete()
    messages.success(request,"Successfull Deleted!")
    return redirect('query-classroom')        

@login_required(login_url='login')
def delete_enrollments(request):
    return render(request, 'delete-enrollments.html')

@login_required(login_url='login')
def delete_users(request):
    return render(request, 'delete-users.html')

@login_required(login_url='login')
def delete_profiles(request):
    return render(request, 'delete-profiles.html')

@login_required(login_url='login')
def delete_parents(request):
    return render(request, 'delete-parents.html')

@login_required(login_url='login')
def delete_zipcode(request):
    return render(request, 'delete-zipcode.html')

@login_required(login_url='login')
def edit_student(request):
    return render(request, 'edit-student.html')

@login_required(login_url='login')
def edit_class(request):
    return render(request, 'edit-class.html')

@login_required(login_url='login')
def edit_schedule(request):
    return render(request, 'edit-schedule.html')

@login_required(login_url='login')
def edit_classroom(request, id):
    classroom = Classroom.objects.get(id=id)
    form = ClassroomForm(request.POST or None, instance=classroom)
    data = {}
    data['classroom'] = classroom
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('query-classroom')
    else:
        form = ClassroomForm
        return render(request, 'edit-classroom.html', data)

@login_required(login_url='login')
def edit_enrollments(request):
    return render(request, 'edit-classroom.html')

@login_required(login_url='login')
def edit_users(request):
    return render(request, 'edit-users.html')

@login_required(login_url='login')
def edit_profiles(request):
    return render(request, 'edit-profiles.html')

@login_required(login_url='login')
def edit_parents(request):
    return render(request, 'edit-parents.html')

@login_required(login_url='login')
def edit_zipcode(request):
    return render(request, 'edit-zipcode.html')

def search_classroom(request):
    search = request.GET.get('search')
    classrooms = Classroom.objects.filter(name__icontains=search)
    form = ClassroomForm()
    data = {}
    data['classrooms'] = classrooms
    data['form'] = form
    return render(request, 'query-classroom.html', data)

def v_login(request):
    return render(request, 'login.html')

def v_authenticate(request):
    v_user = request.POST['username']
    v_pwd = request.POST['password']

    user = authenticate(username=v_user, password=v_pwd)
    
    if user is not None:
        if user.is_active:
            #Redirection to the page successfully.
            login(request, user)
            return render(request, 'index.html')
        else:
            print("Account disabled")
            #Redirection to a page of unactive account.
    else:
       # print("invalid Login/Password ")
        return HttpResponse('login/ senha invalidos')
        #Redirect to invalid login.

def v_logout(request):
    logout(request)
    return render(request, 'login.html')

def recover_password(request):
    return render(request, 'recover-password.html')

def error400(request, exception):
    return render(request, 'error400.html', status=400)

def error403(request, exception):
    return render(request, 'error403.html', status=403)

def error404(request, exception):
    return render(request, 'error404.html', status=404)

def error500(request, exception):
    return render(request, 'error500.html', status=500)