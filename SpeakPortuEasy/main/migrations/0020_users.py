# Generated by Django 5.0.2 on 2024-03-29 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('is_superuser', models.BooleanField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
