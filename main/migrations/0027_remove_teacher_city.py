# Generated by Django 5.0.2 on 2024-11-02 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_teacher_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='city',
        ),
    ]
