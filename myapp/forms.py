from django import forms
from .models import Course , SessionYearModel



class DateInput(forms.DateInput):
    input_type = "date"
    

class AddStudentForm(forms.Form):
    email = forms.EmailField(max_length=50 )
    password = forms.CharField(  max_length=55)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=55)
    username = forms.CharField(max_length=55)
    address = forms.CharField(max_length=55)
    
    try:
        courses = Course.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id , course.course_name)
            course_list.append(single_course)
    except:
        print("here")
        course_list = []
        
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id , str(session_year.session_start_year)+"to"+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
    except:
        session_year_list = []
    
    gender_list = (
        ('MALE' , 'MALE'),
        ('FEMALE', 'FEMALE')
    )
    course_id = forms.ChoiceField(choices=course_list)
    gender = forms.ChoiceField(choices=gender_list)
    session_year_id = forms.ChoiceField(choices=session_year_list)
    profile_pic = forms.FileField(required=False)


class EditStudentForm(forms.Form):
    email = forms.EmailField(max_length=55)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=55)
    username = forms.CharField(max_length=55)
    address = forms.CharField(max_length=55)

    try:
        courses = Course.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id , course.course_name)
            course_list.append(single_course)
    except:
        print("here")
        course_list = []
        
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id , str(session_year.session_start_year)+"to"+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
    except:
        session_year_list = []
    
    gender_list = (
        ('MALE' , 'MALE'),
        ('FEMALE', 'FEMALE')
    )
    course_id = forms.ChoiceField(choices=course_list)
    gender = forms.ChoiceField(choices=gender_list)
    session_year_id = forms.ChoiceField(choices=session_year_list)
    profile_pic = forms.FileField(required=False)