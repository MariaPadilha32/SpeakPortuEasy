# Generated by Django 5.0.2 on 2024-03-29 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_classes_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='under_age',
            field=models.BooleanField(blank=True),
        ),
    ]
