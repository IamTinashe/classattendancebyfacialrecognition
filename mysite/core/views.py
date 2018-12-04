from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from datetime import datetime, timedelta


import json
import os
import time


from mysite.core.forms import SignUpForm
from mysite.core.forms import AddDepartment
from mysite.core.models import Department
from mysite.core.forms import AddStudents
from mysite.core.models import Students
from mysite.core.models import Room
from mysite.core.models import Course
from mysite.core.models import Lecture
from mysite.core.models import Process_Status
from mysite.core.models import Processes
from mysite.core.models import Class_Attendees


import cv2
import cognitive_face as CF
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile



@login_required
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def admin(request):
    departments = Department.objects.all()
    rooms = Room.objects.all()
    courses = Course.objects.all()
    lectures = Lecture.objects.all()
    attendees = Class_Attendees.objects.all()

    All_Students = Students.objects.all()

    date = datetime.now().strftime("%Y-%m-%d")
    p, created = Process_Status.objects.get_or_create(process_date=date)
    p.save()

    return render(request, 'admin.html', {'departments': departments, 'rooms': rooms, 'courses': courses, 'lectures': lectures, 'All_Students': All_Students, 'Process_Status': p, 'attendees': attendees,})

@login_required
def panel(request):
    return render(request, 'panel.html')
        

@login_required
def add_department(request):
    if request.method == 'POST':
        department = request.POST['department']
        p = Department(department_name=department)
        p.save()
    return HttpResponseRedirect('/admin/')


@login_required
def add_room(request):
    if request.method == 'POST':
        building = request.POST['building']
        room = request.POST['room']
        p = Room(building_name=building, room_name=room,)
        p.save()
        
    return HttpResponseRedirect('/admin/')

@login_required
def add_course(request):
    if request.method == 'POST':
        department = request.POST['department']
        course = request.POST['course']
        course_code = request.POST['course_code']
        lecturer = request.POST['lecturer']
        year = request.POST['year']

        department_id = Department.objects.get(department_name=department)
        p = Course(department_id=department_id.id, course_name=course, course_code=course_code, course_year=year, course_lecturer=lecturer)
        p.save()
    return HttpResponseRedirect('/admin/')

@login_required
def add_lecture(request):
    if request.method == 'POST':
        departmentid = request.POST['departmentid']
        courseid = request.POST['courseid']
        roomid = request.POST['roomid']
        date = request.POST['date']
        time = request.POST['time']
        p = Lecture(department_id=departmentid, course_id=courseid, room_id=roomid, date=date, time=time,)
        p.save()
    return HttpResponseRedirect('/admin/')


@login_required
def add_student(request):
    if request.method == 'POST':
        student_number = request.POST['student_number']
        student_name = request.POST['student_name']
        student_surname = request.POST['student_surname']
        student_year = request.POST['student_year']
        department_id = request.POST['departmentid']
        img = request.FILES['student_picture']

        img_extension = os.path.splitext(img.name)[1]
        user_folder = 'mysite/core/static/StudentImages/' + str(student_number)
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        image_path = 'StudentImages/' + str(student_number) + '/student_picture' + img_extension
        img_save_path = user_folder + '/student_picture' + img_extension
        with open(img_save_path, 'wb+') as f:
            for chunk in img.chunks():
                f.write(chunk)
        p = Students(student_number=student_number, student_name=student_name, student_surname=student_surname, student_year=student_year, student_picture=image_path, department_id=department_id,)
        p.save()
        
    return HttpResponseRedirect('/admin/')

@login_required
def start(request):
    request.GET['request_data']
    a = request.GET['request_data']
    status = True
    date = datetime.now().strftime("%Y-%m-%d")

    if a == 'Start_Processes':
        p, created = Process_Status.objects.get_or_create(process_date=date)
        p.save()

        t = Process_Status.objects.get(process_date=date)
        t.process_status = status
        t.save()

        while True:
            print("Running")
            t = Process_Status.objects.get(process_date=date)
            status = t.process_status
            if status == False:
                print("Exiting")
                break
            else:
                lectures = Lecture.objects.all().filter(date=date).values()
                current_time = datetime.now().time()
                for x in lectures:
                    start_time = x.get('time')
                    end_time = x.get('end_time')
                    lecture_id = x.get('id')
                    course_id = x.get('course_id')
                    room_id = x.get('room_id')
                    status = True


                    if start_time >= current_time:
                        processes, created = Processes.objects.update_or_create(lecture_id=lecture_id, defaults={"course_id": course_id, "room_id": room_id, "status": status})
                        processes.save()

                        KEY = '6e59a9ae0dc941e482e22fe58c936533' 
                        CF.Key.set(KEY)

                        BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
                        CF.BaseUrl.set(BASE_URL)

                        camera_port = 0
                        ramp_frames = 6
                        camera = ''

                        def get_image():
                            camera_port = 0
                            camera = cv2.VideoCapture(camera_port)
                            retval, im = camera.read()
                            return im

                        for i in xrange(ramp_frames):
                            temp = get_image()

                        print("Taking image...")

                        camera_capture = get_image()
                        file = "image.png"

                        cv2.imwrite(file, camera_capture)
                        del(camera)
                        
                        students = Students.objects.all().values()
                        for student in students:
                            student_number = student.get('student_number')
                            student_name = student.get('student_name')
                            student_surname = student.get('student_surname')
                            student_image = student.get('student_picture')
                            student_image = 'mysite/core/static/' + str(student_image) 

                            img_urls = ['image1.JPG',student_image ]

                            faces = [CF.face.detect(img_url) for img_url in img_urls]
                            print('Checking: ' + student_name + ' ' + student_surname)
                            for x in range(0, len(faces[0])):
                                similarity = CF.face.verify(faces[0][x]['faceId'], faces[1][0]['faceId'])
                                confidence = similarity.get('confidence')
                                if confidence > 0.4:
                                    attendees, created = Class_Attendees.objects.get_or_create(process_id=processes.id, lecture_id=lecture_id, student_number=student_number,)
                                    attendees.save()
                                    print('Match')
                                else:
                                    print('Does not match')

                            print('=====================================================')

                            time.sleep(5)


            time.sleep(5)
    return HttpResponseRedirect('/admin/')
   

@login_required  
def end(request):
    status = False
    date = datetime.now().strftime("%Y-%m-%d")
    p, created = Process_Status.objects.update_or_create(process_date=date, defaults={"process_status": status})
    p.save()
    return HttpResponseRedirect('/admin/')
    