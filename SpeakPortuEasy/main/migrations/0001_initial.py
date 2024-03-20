# Generated by Django 5.0.2 on 2024-03-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
                ('is_online', models.BooleanField()),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'classroom',
            },
        ),
    ]