from django.urls import path, include
from School_App import views

app_name='School_App'
urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('enroll',views.enroll,name='enroll'),
    path('add/',views.StudentCreateView.as_view(),name='student_add'),
    path('ajax/load-course',views.load_courses,name='ajax_load_courses'),
    ]