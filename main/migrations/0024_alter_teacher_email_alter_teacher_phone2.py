# Generated by Django 5.0.2 on 2024-10-27 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_remove_parents_student_alter_classes_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]