from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from main.models import Classroom
from .forms import ClassroomForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('Hello World - Welcome to Django Framework')

@login_required(login_url='login')
def register_student(request):
    return render(request, 'register-student.html')

@login_required(login_url='login')
def register_class(request):
    return render(request, 'register-class.html')

@login_required(login_url='login')
def register_schedule(request):
    return render(request, 'register-schedule.html')

@login_required(login_url='login')
def register_classroom(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        count = Classroom.objects.filter(name=name).count()
        if count > 0:
            messages.error(request, 'There is a Classroom registered with that name, please use a different name.')
            return redirect('register-classroom')
        if request.method == 'POST':
            form = ClassroomForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('query-classroom')
            else:
                return redirect('register-classroom')
    else:
        form = ClassroomForm
        return render(request, 'register-classroom.html', {'form' : form})

@login_required(login_url='login')
def register_enrollments(request):
    return render(request, 'register-classroom.html')

def register_users(request):
    return render(request, 'register-users.html')

@login_required(login_url='login')
def register_profiles(request):
    return render(request, 'register-profiles.html')

@login_required(login_url='login')
def register_parents(request):
    return render(request, 'register-parents.html')

@login_required(login_url='login')
def register_zipcode(request):
    return render(request, 'register-zipcode.html')

@login_required(login_url='login')
def query_class(request):
    return render(request, 'query-class.html')

@login_required(login_url='login')
def query_classroom(request):
    form = ClassroomForm
    classrooms = Classroom.objects.all()
    total = Classroom.objects.count()
    list_classroom = Classroom.objects.all()
    paginator = Paginator(list_classroom, 4)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'query-classroom.html', {'form': form, 'classrooms': classrooms, 'total': total, 'page_obj': page_obj})

@login_required(login_url='login')
def query_enrollments(request):
    return render(request, 'query-enrollments.html')

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

@login_required(login_url='login')
def delete_classroom(request):
    return render(request, 'delete-classroom.html')

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