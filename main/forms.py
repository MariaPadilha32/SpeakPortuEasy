from django.forms import ModelForm
from .models import Classroom, Classes, Enrollments
from .models import Parents, Student, Schedule, Teacher, Users


class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = '__all__'


class ClassesForm(ModelForm):
    class Meta:
        model = Classes
        fields = '__all__'


class EnrollmentsForm(ModelForm):
    class Meta:
        model = Enrollments
        fields = '__all__'


class ParentsForm(ModelForm):
    class Meta:
        model = Parents
        fields = '__all__'


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
