# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_Attendees',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('process_id', models.IntegerField()),
                ('lecture_id', models.IntegerField()),
                ('student_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department_id', models.IntegerField(null=True)),
                ('course_name', models.CharField(max_length=120)),
                ('course_code', models.CharField(max_length=120, null=True)),
                ('course_year', models.IntegerField(null=True)),
                ('course_lecturer', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department_id', models.IntegerField()),
                ('course_id', models.IntegerField()),
                ('room_id', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('end_time', models.TimeField(default='17:15:00')),
                ('duration', models.DurationField(default=datetime.timedelta(0, 7200))),
            ],
        ),
        migrations.CreateModel(
            name='Process_Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('process_date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('process_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Processes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lecture_id', models.IntegerField()),
                ('course_id', models.IntegerField()),
                ('room_id', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('building_name', models.CharField(max_length=120)),
                ('room_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_number', models.IntegerField()),
                ('student_name', models.CharField(max_length=120)),
                ('student_surname', models.CharField(max_length=120)),
                ('student_year', models.IntegerField(null=True)),
                ('student_picture', models.CharField(max_length=120, null=True)),
                ('department_id', models.IntegerField(null=True)),
            ],
        ),
    ]
