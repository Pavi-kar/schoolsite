from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from . models import Student, Course
from . forms import StudentForm

# Create your views here.
def home(request):
    
    return render(request,"index.html")



# Create your views here.
def register(request):
    if request.method=='POST':
        uname=request.POST['uname']
        passwd=request.POST['password']
        passwd1=request.POST['cpassword']
        if passwd == passwd1:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"User name already taken!")
                return redirect('School_App:register')
            else:
                user=User.objects.create_user(username=uname,
                                              password=passwd)
                user.save()
                print("User created")
                return redirect('School_App:login')
        else:
            messages.info(request,"Password not matched!")
            return redirect('School_App:register')
        return redirect('/')
    else:
        return render(request,"register.html")

def login(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['password']
        user=auth.authenticate(username=uname,password=passwd)
        if user is not None:
            auth.login(request,user)
            return redirect('School_App:enroll')
        else:
            messages.info(request,"Invalid credentials!")
            return redirect('School_App:login')
    return render(request,"login.html")

def enroll(request):
    return render(request,"enroll.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

class StudentCreateView(SuccessMessageMixin,CreateView):
    model = Student

    form_class = StudentForm
    
    template_name = 'enroll_form.html'
    
    def get_success_url(self):
        return reverse_lazy('School_App:student_add')
    
    success_message = "Enquiry Registered Successfully. Our Team will Contact You Soon..."
    

def load_courses(request):
    department_id = request.GET.get('department')
    courses = Course.objects.filter(department_id=department_id).order_by('name')
    return render(request,'myuser/course_dropdown_list_options.html',{'courses': courses})