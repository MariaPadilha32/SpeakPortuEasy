from django.contrib import admin
from .models import Classroom, Classes, ZipCode, Enrollments, Parents, Student, Profiles, Schedule

# Register your models here.
admin.site.register(Classroom)
admin.site.register(Classes)
admin.site.register(ZipCode)
admin.site.register(Enrollments)
admin.site.register(Parents)
admin.site.register(Student)
admin.site.register(Profiles)
admin.site.register(Schedule)
