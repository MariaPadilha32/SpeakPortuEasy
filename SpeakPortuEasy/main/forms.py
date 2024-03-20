from django.forms import ModelForm
from .models import Classroom, Classes, ZipCode, Enrollments, Parents, Student, Profiles, Schedule

class ClassroomForm(ModelForm):
    class Meta: # using Meta database
        model = Classroom  
        fields = '__all__'

class ClassesForm(ModelForm):
    class Meta:
        model = Classes
        fields = '__all__'

class ZipCodeForm(ModelForm):
    class Meta:
        model = ZipCode
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

class ProfilesForm(ModelForm):
    class Meta:
        model = Profiles
        fields = '__all__'

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
