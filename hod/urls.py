from django.urls import path
from .import views



urlpatterns = [
    
    # URL for Admin
    path('admin_home/', views.admin_home, name="admin_home"),
    
    #STAFF ACTIONS URLS
    path('user_profile_view/', views.user_profile_view, name="profile"),
    
    path('add_staff/', views.add_staff, name="add_staff"),
    path('list_staff/', views.list_staff, name="list_staff"),
    path('detail_staff/', views.detail_staff, name="detail_staff"),
    path('edit_staff/', views.edit_staff, name="edit_staff"),

    #STUDENTS ACTIONS URLS
    path('add_student/', views.add_student, name="add_student"),
    path('list_student/', views.list_student, name="list_student"),
    path('detail_student/', views.detail_student, name="detail_student"),
    path('edit_student/', views.edit_student, name="edit_student"),
    
    #DEPARTMENT ACTIONS URLS 
    path('list_depart/', views.list_depart, name="list_depart"),
    path('add_depart/', views.add_depart, name="add_depart"),
    path('edit_depart/', views.edit_depart, name="edit_depart"),
    
    #SUBJECT ACTION URLS
    path('add_subject/', views.add_subject, name="add_subject"),
    path('edit_subject/', views.edit_subject, name="edit_subject"),
    path('list_subject/', views.list_subject, name="list_subject"),
    
    
    # MANAGEMENT URLS FOR ACCOUNTS SETTINGS
    path('fees/', views.fees, name="fees"),

    path('fees_collect/', views.fees_collect, name="fees_collect"),
    path('add_fees/', views.add_fees, name="add_fees"),
    path('expenses/', views.expenses, name="expenses"),
    path('salary/', views.salary, name="salary"),
    path('add_salary/', views.add_salary, name="add_salary"),
    path('add_expenses/', views.add_expenses, name="add_expenses"),
    
    
    #HOLIDAYS
    path('holiday/', views.holiday, name="holiday"),
    path('exam_list/', views.exam_list, name="exam_list"),
    
  
    ]
