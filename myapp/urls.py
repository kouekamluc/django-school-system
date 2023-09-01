from django.urls import path  
from .import views 
from .import HodViews , StaffViews , StudentViews

urlpatterns = [
    path('' ,views.home, name='home'),
    path('contact', views.contact, name="contact"),
    path('login', views.loginUser, name="login"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('registration', views.registration, name="registration"),
    path('doLogin', views.doLogin, name="doLogin"),
    path('doRegistration', views.doRegistration, name="doRegistration"),
     
    
]
