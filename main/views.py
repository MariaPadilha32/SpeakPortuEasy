from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from main.models import Classroom, Student, Enrollments
from main.models import Classes, Schedule, Parents, Teacher
from .forms import ClassroomForm, StudentForm, EnrollmentsForm, UserForm
from .forms import ClassesForm, ScheduleForm, ParentsForm, TeacherForm

# Create your views here.


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('Hello World - Welcome to Django Framework')


@login_required(login_url='login')
def register_student(request):
    parents = Parents.objects.all().order_by('name')
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('query-student')
        else:
            return redirect('home')
    else:
        form = StudentForm()
        return render(
        request,
        'register-student.html',
        {'form': form, 'parents': parents}
    )


@login_required(login_url='login')
def register_class(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        count = Classes.objects.filter(name=name).count()
        if count > 0:
            messages.error(
                request,
                'There is a class with that name, please use a different name.'
            )
            return redirect('register-class')
        if request.method == 'POST':
            form = ClassesForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('query-class')
            else:
                return redirect('register-class')
    else:
        form = ClassesForm()
        return render(request, 'register-class.html', {'form': form})


@login_required(login_url='login')
def register_schedule(request):
    classes = Classes.objects.all().order_by('name')
    if request.method == 'POST':
        id = request.POST.get('id')
        count = Schedule.objects.filter(id=id).count()
        if count > 0:
            messages.error(
                request,
                'No schedule available, please try a different time.'
            )
            return redirect('register-schedule')
        if request.method == 'POST':
            form = ScheduleForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('query-schedule')
            else:
                return redirect('register-schedule')
    else:
        form = ScheduleForm()
        return render(
            request,
            'register-schedule.html',
            {
                'form': form,
                'classes': classes
            }
        )


@login_required(login_url='login')
def register_classroom(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        count = Classroom.objects.filter(name=name).count()
        if count > 0:
            messages.error(
                request,
                'Classroom name exists, please use another.'
            )
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
        return render(request, 'register-classroom.html', {'form': form})


@login_required(login_url='login')
def register_enrollments(request):
    students = Student.objects.all().order_by('name')
    classes = Classes.objects.all().order_by('name')
    if request.method == 'POST':
        student_id = request.POST.get('student')
        class_id = request.POST.get('classname')
        count = Enrollments.objects.filter(student=student_id, classname=class_id).count()
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
        return render(
            request,
            'register-enrollments.html',
            {
                'form': form,
                'students': students,
                'classes': classes
            }
        )


@login_required(login_url='login')
def register_parents(request):
    if request.method == 'POST':
        form = ParentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('query-parents')
        else:
            return redirect('register-parents')
    else:
        form = ParentsForm()
        return render(request, 'register-parents.html', {'form': form})


@login_required(login_url='login')
def register_teacher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        count = Teacher.objects.filter(name=name).count()
        if count > 0:
            messages.error(
                request,
                'That name is already used, please use a different name.'
            )
            return redirect('register-teacher')

        if request.method == 'POST':
            form = TeacherForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('query-teacher')
        else:
            return redirect('register-teacher')
    else:
        form = TeacherForm()
        return render(request, 'register-teacher.html', {'form': form})


@login_required(login_url='login')
def query_class(request):
    form = ClassesForm
    classes = Classes.objects.all()
    total = Classes.objects.count()
    list_classes = Classes.objects.all()
    paginator = Paginator(list_classes, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(
        request,
        'query-class.html',
        {
            'form': form,
            'classes': classes,
            'total': total,
            'page_obj': page_obj
        }
    )


@login_required(login_url='login')
def query_classroom(request):
    form = ClassroomForm
    classrooms = Classroom.objects.all()
    total = Classroom.objects.count()
    list_classroom = Classroom.objects.all()
    paginator = Paginator(list_classroom, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(
        request,
        'query-classroom.html',
        {
            'form': form,
            'classrooms': classrooms,
            'total': total,
            'page_obj': page_obj
        }
    )


@login_required(login_url='login')
def query_enrollments(request):
    form = EnrollmentsForm
    enrollments = Enrollments.objects.all()
    total = Enrollments.objects.count()
    list_enrollments = Enrollments.objects.all()
    paginator = Paginator(list_enrollments, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(
        request,
        'query-enrollments.html',
        {
            'form': form,
            'enrollments': enrollments,
            'total': total,
            'page_obj': page_obj
        }
    )


@login_required(login_url='login')
def query_parents(request):
    form = ParentsForm
    parents = Parents.objects.all()
    total = Parents.objects.count()
    list_parents = Parents.objects.all()
    paginator = Paginator(list_parents, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(
        request,
        'query-parents.html',
        {
            'form': form,
            'parents': parents,
            'total': total,
            'page_obj': page_obj
        }
    )


@login_required(login_url='login')
def query_schedule(request):
    form = ScheduleForm
    schedule = Schedule.objects.all()
    total = Schedule.objects.count()
    list_schedule = Schedule.objects.all()
    paginator = Paginator(list_schedule, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(
        request,
        'query-schedule.html',
        {
            'form': form,
            'schedule': schedule,
            'total': total,
            'page_obj': page_obj
        }
    )


@login_required(login_url='login')
def query_student(request):
    form = StudentForm
    students = Student.objects.all()
    total = Student.objects.count()
    list_students = Student.objects.all()
    paginator = Paginator(list_students, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(
        request,
        'query-student.html',
        {
            'form': form,
            'students': students,
            'total': total,
            'page_obj': page_obj
        }
    )


@login_required(login_url='login')
def query_users(request):
    form = UsersForm
    users = Users.objects.all()
    total = Users.objects.count()
    list_users = Users.objects.all()
    paginator = Paginator(list_users, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(
        request,
        'query-users.html',
        {
            'form': form,
            'users': users,
            'total': total,
            'page_obj': page_obj
        }
    )


@login_required(login_url='login')
def query_teacher(request):
    form = TeacherForm
    teachers = Teacher.objects.all()
    total = Teacher.objects.count()
    list_teachers = Teacher.objects.all()
    paginator = Paginator(list_teachers, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(
        request,
        'query-teacher.html',
        {
            'form': form,
            'teachers': teachers,
            'total': total,
            'page_obj': page_obj
        }
    )


@login_required(login_url='accounts/login')
def delete_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)
    data = {}
    data['student'] = student
    data['form'] = form
    if request.method == "POST":
        student.delete()
        messages.success(request, "Successfull Deleted!")
        return redirect('query-student')
    else:
        return render(request, 'delete-student.html', data)


@login_required(login_url='accounts/login')
def delete_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    form = TeacherForm(request.POST or None, instance=teacher)
    data = {}
    data['teacher'] = teacher
    data['form'] = form
    if request.method == "POST":
        teacher.delete()
        messages.success(request, "Successfull Deleted!")
        return redirect('query-teacher')
    else:
        return render(request, 'delete-teacher.html', data)


@login_required(login_url='accounts/login')
def delete_class(request, id):
    classes = Classes.objects.get(id=id)
    form = ClassesForm(request.POST or None, instance=classes)
    data = {}
    data['classes'] = classes
    data['form'] = form
    if request.method == "POST":
        classes.delete()
        messages.success(request, "Successfull Deleted!")
        return redirect('query-class')
    else:
        return render(request, 'delete-class.html', data)


@login_required(login_url='accounts/login')
def delete_schedule(request, id):
    schedule = Schedule.objects.get(id=id)
    classes = Classes.objects.get(id=schedule.student)
    form = ScheduleForm(request.POST or None, instance=schedule)
    data = {}
    data['schedule'] = schedule
    data['form'] = form
    data['classes'] = classes
    if request.method == "POST":
        schedule.delete()
        messages.success(request, "Successfull Deleted!")
        return redirect('query-schedule')
    else:
        return render(request, 'delete-schedule.html', data)


@login_required(login_url='accounts/login')
def delete_classroom(request, id):
    classroom = Classroom.objects.get(id=id)
    form = ClassroomForm(request.POST or None, instance=classroom)
    data = {}
    data['classroom'] = classroom
    data['form'] = form
    if request.method == "POST":
        classroom.delete()
        messages.success(request, "Successfull Deleted!")
        return redirect('query-classroom')
    else:
        return render(request, 'delete-classroom.html', data)


@login_required(login_url='accounts/login')
def delete_enrollments(request, id):
    enrollments = Enrollments.objects.get(id=id)
    form = EnrollmentsForm(request.POST or None, instance=enrollments)
    data = {}
    data['enrollments'] = enrollments
    data['form'] = form
    if request.method == "POST":
        enrollments.delete()
        messages.success(request, "Successfull Deleted!")
        return redirect('query-enrollments')
    else:
        return render(request, 'delete-enrollments.html', data)


@login_required(login_url='accounts/login')
def delete_users(request, id):
    users = Users.objects.get(id=id)
    form = UsersForm(request.POST or None, instance=users)
    data = {}
    data['users'] = users
    data['form'] = form
    if request.method == "POST":
        users.delete()
        messages.success(request, "Successfull Deleted!")
        return redirect('query-users')
    else:
        return render(request, 'delete-users.html', data)


@login_required(login_url='accounts/login')
def delete_parents(request, id):
    parents = Parents.objects.get(id=id)
    form = ParentsForm(request.POST or None, instance=parents)
    data = {}
    data['parents'] = parents
    data['form'] = form
    if request.method == "POST":
        parents.delete()
        messages.success(request, "Successfull Deleted!")
        return redirect('query-parents')
    else:
        return render(request, 'delete-parents.html', data)


@login_required(login_url='login')
def query_teacher(request):
    form = TeacherForm
    teachers = Teacher.objects.all()
    total = Teacher.objects.count()
    list_teachers = Teacher.objects.all()
    paginator = Paginator(list_teachers, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(
        request,
        'query-teacher.html',
        {
            'form': form,
            'teachers': teachers,
            'total': total,
            'page_obj':  page_obj
        }
    )


@login_required(login_url='login')
def edit_student(request, id):
    student = Student.objects.get(id=id)
    parents = Parents.objects.all()
    form = StudentForm(request.POST or None, instance=student)
    data = {}
    data['student'] = student
    data['parents'] = parents
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('query-student')
        else:
            return render(request, 'edit_student.html', data)
    else:
        form = StudentForm
        return render(request, 'edit-student.html', data)


@login_required(login_url='login')
def edit_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    form = TeacherForm(request.POST or None, instance=teacher)
    data = {}
    data['teacher'] = teacher
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('query-teacher')
        else:
            return render(request, 'edit-teacher.html', data)
    else:
        form = TeacherForm
        return render(request, 'edit-teacher.html', data)


@login_required(login_url='login')
def edit_class(request, id):
    classes = Classes.objects.get(id=id)
    form = ClassesForm(request.POST or None, instance=classes)
    data = {}
    data['classes'] = classes
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('query-class')
        else:
            return render(request, 'edit_class.html', data)
    else:
        form = ClassesForm
        return render(request, 'edit-class.html', data)


@login_required(login_url='login')
def edit_schedule(request, id):
    schedule = Schedule.objects.get(id=id)
    classes = Classes.objects.all().order_by('name')
    form = ScheduleForm(request.POST or None, instance=schedule)
    data = {}
    data['schedule'] = schedule
    data['form'] = form
    data['classes'] = classes
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('query-schedule')
        else:
            return render(request, 'edit-schedule.html', data)
    else:
        form = ScheduleForm
        return render(request, 'edit-schedule.html', data)


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
            return render(request, 'edit-classroom.html', data)
    else:
        form = ClassroomForm
        return render(request, 'edit-classroom.html', data)


@login_required(login_url='login')
def edit_enrollments(request, id):
    enrollments = Enrollments.objects.get(id=id)
    students = Student.objects.all()
    classes = Classes.objects.all()
    form = EnrollmentsForm(request.POST or None, instance=enrollments)
    data = {}
    data['enrollments'] = enrollments
    data['form'] = form
    data['students'] = students
    data['classes'] = classes
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('query-enrollments')
        else:
            return render(request, 'edit-enrollments.html', data)
    else:
        form = EnrollmentsForm
        return render(request, 'edit-enrollments.html', data)


@login_required(login_url='login')
def edit_users(request, id):
    users = Users.objects.get(id=id)
    form = UsersForm(request.POST or None, instance=users)
    data = {}
    data['users'] = users
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('query-users')
        else:
            return render(request, 'edit-users.html', data)
    else:
        form = UsersForm
        return render(request, 'edit-users.html', data)


@login_required(login_url='login')
def edit_parents(request, id):
    parents = Parents.objects.get(id=id)
    form = ParentsForm(request.POST or None, instance=parents)
    data = {}
    data['parents'] = parents
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('query-parents')
        else:
            return render(request, 'edit-parents.html', data)
    else:
        form = ParentsForm
    return render(request, 'edit-parents.html', data)


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
            # Redirection to the page successfully.
            login(request, user)
            return render(request, 'index.html')
        else:
            print("Account disabled")
            # Redirection to a page of unactive account.
    else:
        # print("invalid Login/Password ")
        return HttpResponse('login/ senha invalidos')
        # Redirect to invalid login.


def v_logout(request):
    logout(request)
    return render(request, 'login.html')


def recover_password(request):
    return render(request, 'recover-password.html')


def search_classroom(request):
    query = request.GET.get('search')
    classrooms = Classroom.objects.filter(name__icontains=query)
    return render(request, 'query-classroom.html', {'classes': classrooms})


def search_class(request):
    query = request.GET.get('search')
    classname = Classes.objects.filter(name__icontains=query)
    return render(request, 'query-class.html', {'classnames': classname})


def search_student(request):
    query = request.GET.get('search')
    student = Student.objects.filter(name__icontains=query)
    total_students = student.count()
    return render(request, 'query-student.html', {'students': student, 'total_student' : total_students})


def search_enrollments(request):
    query = request.GET.get('search')
    enrollment = Enrollments.objects.filter(name__icontains=query)
    return render(
        request,
        'query-enrollments.html',
        {
            'enrollments': enrollment
        }
    )


def search_parents(request):
    query = request.GET.get('search')
    parent = Parents.objects.filter(name__icontains=query)
    return render(request, 'query-parents.html', {'parents': parent})


def search_teacher(request):
    query = request.GET.get('search')
    teacher = Teacher.objects.filter(name__icontains=query)
    return render(request, 'query-teacher.html', {'teachers': teacher})


def search_schedule(request):
    query = request.GET.get('search')
    schedules = Schedule.objects.filter(name__icontains=query)
    return render(request, 'query-schedule.html', {'schedule': schedules})


def v_404(request, exception):
    return render(request, "eror404.html", status=404)


def v_500(request):
    return render(request, "eror500.html", status=500)
