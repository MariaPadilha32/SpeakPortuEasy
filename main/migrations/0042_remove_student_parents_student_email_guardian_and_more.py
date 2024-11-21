# Generated by Django 5.0.2 on 2024-11-20 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_remove_classroom_author_remove_enrollments_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='parents',
        ),
        migrations.AddField(
            model_name='student',
            name='email_guardian',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='name_guardian',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone1_guardian',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone2_guardian',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]