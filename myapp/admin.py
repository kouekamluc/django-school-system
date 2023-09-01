from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser , AdminHOD , Staff , Course ,Student ,Subject , Attendance ,AttendanceReport , LeaveReportStaff ,LeaveReportStudent ,FeedBackStaff,FeedBackStudent , NotificationStaff ,NotificationStudent ,SessionYearModel
from .forms import CustomUserChangeForm , CustomUserCreationForm
# Register your models here.



class UserModel(UserAdmin):
    add_form  = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser 
    list_display = ('username','email' , 'user_type' , 'is_staff' , 'is_active')
    fieldsets = (
        *UserAdmin.fieldsets ,
        ('Other Personal info',
         {
            "fields": (
                'user_type', 
            ),
        }),
    )
    
    
  
    


admin.site.register(CustomUser , UserModel)

admin.site.register(SessionYearModel)
admin.site.register(AdminHOD)
admin.site.register(Staff)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaff)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaff)