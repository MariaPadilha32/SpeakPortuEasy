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


