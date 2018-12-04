from __future__ import unicode_literals
from django.db import models
from PIL import Image
from datetime import timedelta
from datetime import datetime

class Department(models.Model):
	department_name = models.CharField(max_length=120)

	def __str__(self):
		return self.department_name

class Room(models.Model):
	building_name = models.CharField(max_length=120)
	room_name = models.CharField(max_length=60)

	def __str__(self):
		return u'%s %s' % (self.building_name, self.room_name)

class Course(models.Model):
	department_id = models.IntegerField(null=True)
	course_name = models.CharField(max_length=120)
	course_code = models.CharField(null=True, max_length=120)
	course_year = models.IntegerField(null=True)
	course_lecturer = models.CharField(max_length=120)

class Lecture(models.Model):
	department_id = models.IntegerField()
	course_id = models.IntegerField()
	room_id = models.IntegerField()
	date = models.DateField()
	time = models.TimeField()
	end_time = models.TimeField(default='17:15:00')
	duration = models.DurationField(default=timedelta(minutes=120))

class Processes(models.Model):
	lecture_id = models.IntegerField()
	course_id = models.IntegerField()
	room_id = models.IntegerField()
	status = models.BooleanField(default=False)

class Students(models.Model):
	student_number = models.IntegerField()
	student_name = models.CharField(max_length=120)
	student_surname = models.CharField(max_length=120)
	student_year = models.IntegerField(null=True)
	student_picture = models.CharField(null=True, max_length=120)
	department_id = models.IntegerField(null=True)

class Process_Status(models.Model):
	process_date = models.DateTimeField(default=datetime.now, blank=True)
	process_status = models.BooleanField(default=False)

class Class_Attendees(models.Model):
	process_id = models.IntegerField()
	lecture_id = models.IntegerField()
	student_number = models.IntegerField()
	
