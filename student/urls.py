from django.urls import path
from . import views



urlpatterns = [
         # URLS for Student
    path('student_home/', views.student_home, name="student_home"),
    path('student_view_attendance/', views.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post/', views.student_view_attendance_post, name="student_view_attendance_post"),
    path('student_apply_leave/', views.student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save/', views.student_apply_leave_save, name="student_apply_leave_save"),
    path('student_feedback/', views.student_feedback, name="student_feedback"),
    path('student_feedback_save/', views.student_feedback_save, name="student_feedback_save"),
    path('student_profile/', views.student_profile, name="student_profile"),
    path('student_profile_update/', views.student_profile_update, name="student_profile_update"),
    path('student_view_result/', views.student_view_result, name="student_view_result"),
 
 
]
