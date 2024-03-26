from django.contrib import admin
from .models import Classroom, Classes, Enrollments, Parents, Student, Profiles, Schedule, Teacher

# Register your models here.
admin.site.register(Classroom)
admin.site.register(Classes)
admin.site.register(Enrollments)
admin.site.register(Parents)
admin.site.register(Student)
admin.site.register(Profiles)
admin.site.register(Schedule)
admin.site.register(Teacher)
