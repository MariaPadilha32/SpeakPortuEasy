# Generated by Django 5.0.2 on 2024-11-03 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_enrollments_classname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='parents',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.parents'),
        ),
    ]
