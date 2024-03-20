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

