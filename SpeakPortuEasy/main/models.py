from django.db import models

# Create your models here.

class Enrollments(models.Model):
    student = models.CharField(max_length=50, blank=False, null=False)
    classname = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.classname

    class Meta:
        db_table = 'enrollment'

class Classroom(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    capacity = models.IntegerField(blank=False, null=False)
    is_online = models.BooleanField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'classroom'


class Parents(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, blank=False, null=False)
    student = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'parents'


class Student(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    surname = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone1 = models.CharField(max_length=20, blank=False, null=False)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    under_age = models.BooleanField(blank=True)
    parents = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'student'



class Users(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    role = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'


class Teacher(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    surname = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=20, blank=False, null=False)
    phone2 = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'teacher'



class Classes(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    level = models.CharField(max_length=2, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'classes'


class Parents(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, blank=False, null=False)
    student = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'parents'

class Schedule(models.Model):
    day_week = models.CharField(max_length=10, blank=False, null=False)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    student = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.day_week

    class Meta:
        db_table = 'schedule'

class Enrollments(models.Model):
    student = models.CharField(max_length=50, blank=False, null=False)
    classname = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.classname

    class Meta:
        db_table = 'enrollment'
