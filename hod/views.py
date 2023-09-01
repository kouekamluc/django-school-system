from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
 
from myapp.forms import AddStudentForm, EditStudentForm
 
from myapp.models import CustomUser, Staff, Course, Subject, Student, SessionYearModel, FeedBackStudent, FeedBackStaff, LeaveReportStudent, LeaveReportStaff, Attendance, AttendanceReport
 
 
def admin_home(request):
     
    all_student_count = Student.objects.all().count()
    subject_count = Subject.objects.all().count()
    course_count = Course.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_all = Course.objects.all()
    course_name_list = []
    subject_count_list = []
    student_count_list_in_course = []
 
    for course in course_all:
        subjects = Subject.objects.filter(course_id=course.id).count()
        students = Student.objects.filter(course_id=course.id).count()
        course_name_list.append(course.course_name)
        subject_count_list.append(subjects)
        student_count_list_in_course.append(students)
     
    subject_all = Subject.objects.all()
    subject_list = []
    student_count_list_in_subject = []
    for subject in subject_all:
        course = Course.objects.get(id=subject.course_id.id)
        student_count = Student.objects.filter(course_id=course.id).count()
        subject_list.append(subject.subject_name)
        student_count_list_in_subject.append(student_count)
     
    # For Saffs
    staff_attendance_present_list=[]
    staff_attendance_leave_list=[]
    staff_name_list=[]
 
    staffs = Staff.objects.all()
    for staff in staffs:
        subject_ids = Subject.objects.filter(staff_id=staff.admin.id)
        attendance = Attendance.objects.filter(subject_id__in=subject_ids).count()
        leaves = LeaveReportStaff.objects.filter(staff_id=staff.id,
                                                 leave_status=1).count()
        staff_attendance_present_list.append(attendance)
        staff_attendance_leave_list.append(leaves)
        staff_name_list.append(staff.admin.first_name)
 
    # For Students
    student_attendance_present_list=[]
    student_attendance_leave_list=[]
    student_name_list=[]
 
    students = Student.objects.all()
    for student in students:
        attendance = AttendanceReport.objects.filter(student_id=student.id,
                                                     status=True).count()
        absent = AttendanceReport.objects.filter(student_id=student.id,
                                                 status=False).count()
        leaves = LeaveReportStudent.objects.filter(student_id=student.id,
                                                   leave_status=1).count()
        student_attendance_present_list.append(attendance)
        student_attendance_leave_list.append(leaves+absent)
        student_name_list.append(student.admin.first_name)
 
 
    context={
        "all_student_count": all_student_count,
        "subject_count": subject_count,
        "course_count": course_count,
        "staff_count": staff_count,
        "course_name_list": course_name_list,
        "subject_count_list": subject_count_list,
        "student_count_list_in_course": student_count_list_in_course,
        "subject_list": subject_list,
        "student_count_list_in_subject": student_count_list_in_subject,
        "staff_attendance_present_list": staff_attendance_present_list,
        "staff_attendance_leave_list": staff_attendance_leave_list,
        "staff_name_list": staff_name_list,
        "student_attendance_present_list": student_attendance_present_list,
        "student_attendance_leave_list": student_attendance_leave_list,
        "student_name_list": student_name_list,
    }
    return render(request, "hod/admin_dashboard.html", context)
 



#STAFF DATAIL VIEWS 
def user_profile_view(request):
    
     return render(request , 'hod/profile.html')
def add_staff(request):
    return render(request, "hod/add-teacher.html")

def list_staff(request):
    return render(request , 'hod/teachers.html')

def detail_staff(request):
    return render(request , 'hod/teacher-details.html')


def edit_staff(request ):
    return render(request , 'hod/edit-teacher.html') 

 

#STUDENT DETAIL VIEWS 

def add_student(request):
    return render(request , 'hod/add-student.html')

def list_student(request):
    return render(request , 'hod/students.html')

def detail_student(request):
    return render(request , 'hod/student-details.html')


def edit_student(request):
    return render(request , 'hod/edit-student.html')

# DEPARTMENTS VIEWS 

def list_depart(request):
    return render(request  , 'hod/departments.html')

def add_depart(request):
    return render(request  , 'hod/add-department.html')

def edit_depart(request):
    return render(request  , 'hod/edit-department.html')

# SUBJECT ACTION VIEWS


def list_subject(request):
    return render(request  , 'hod/subjects.html')

def add_subject(request):
    return render(request  , 'hod/add-subject.html')

def edit_subject(request):
    return render(request  , 'hod/edit-subject.html')



# MANAGEMENT VIEWS FOR ACCOUNTS 

def fees(request):
    return render(request , 'hod/fees.html')

def fees_collect(request):
    return render(request , 'hod/fees-collections.html')

def add_fees(request):
    return render(request , 'hod/add-fees-collection.html')

def expenses(request):
    return render(request , 'hod/expenses.html')

def salary(request):
    return render(request , 'hod/salary.html')


def add_expenses(request):
    return render(request , 'hod/add-expenses.html')

def add_salary(request):
    return render(request , 'hod/add-salary.html')


#HOLIDAYS
def holiday(request):
    return render(request , 'hod/holiday.html')

def exam_list(request):
    return render(request , 'hod/exam.html')


