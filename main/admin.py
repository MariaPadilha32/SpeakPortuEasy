from django.contrib import admin
from .models import Classroom, Classes, Enrollments
from .models import Student, Schedule, Teacher, Users

# Register your models here.
admin.site.register(Classroom)
admin.site.register(Classes)
admin.site.register(Enrollments)
admin.site.register(Student)
admin.site.register(Schedule)
admin.site.register(Teacher)
admin.site.register(Users)
