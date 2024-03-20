from django.db import models

# Create your models here.

class Classroom(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    capacity = models.IntegerField(blank=False, null=False)
    is_online = models.BooleanField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'classroom'

class Classes(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    level = models.CharField(max_length=2, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    teacher = models.CharField(max_length=50, blank=False, null=False)
    student1 = models.CharField(max_length=50, blank=False, null=False)
    student2 = models.CharField(max_length=50, blank=False, null=False)
    student3 = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'classes'

class ZipCode(models.Model):
    zipcode = models.CharField(max_length=10, unique=True, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)
    country = models.CharField(max_length=50, unique=True, blank=False, null=False)

    def __str__(self) -> str:
        return self.zipcode
    
    class Meta:
        db_table = 'zipcode'
class Enrollments(models.Model):
    student = models.CharField(max_length=50, blank=False, null=False)
    classname = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.classname
    
    class Meta:
        db_table = 'enrollment'

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
    email = models.CharField(max_length=100)
    phone1 = models.CharField(max_length=20, blank=False, null=False)
    phone2 = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10, blank=False, null=False)
    country = models.CharField(max_length=50, blank=False, null=False)
    state = models.CharField(max_length=50, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    adress = models.CharField(max_length=200, blank=False, null=False)
    under_age = models.BooleanField()
    parents = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'student'

class Profiles(models.Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    profile = models.CharField(max_length=50, blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    birthdate = models.DateField(blank=False, null=False)
    gender = models.CharField(max_length=10, blank=False, null=False, choices=GENDER)

    def __str__(self):
        return self.profile
    
    class Meta:
        db_table = 'profiles'

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