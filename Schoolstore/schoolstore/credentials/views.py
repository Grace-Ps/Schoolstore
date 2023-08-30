from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import EnrollmentForm
from .models import Enrollment, Department, Course


# Create your views here.
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('new_page')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")

def register(request):
    if request.method == "POST":
        print("Inside")
        username=request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
           if User.objects.filter(username=username).exists():
              messages.info(request,"username taken")
              return redirect('register')
           else:
               user=User.objects.create_user(username=username,password=password)
               user.save();
               return redirect('login')

        else:
            messages.info(request,"password doesn't match")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
    
    
def home(request):
    return render(request, 'index.html')



def new_page(request):
    return render(request, 'new_page.html')

def form_page(request):
    Departments = Department.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone']
        mail_id = request.POST['email']
        address = request.POST['address']
        department = request.POST['department']
        courses = request.POST['courses']
        purpose = request.POST['purpose']
        materials_provide = request.POST['materials']
        order = Enrollment(name=name, dob=dob, courses=courses,purpose=purpose,age=age,gender=gender,phone_number=phone_number,mail_id=mail_id,address=address,department=department,)
        order.save()
        return redirect('success')
    return render(request, 'form_page.html',{'Departments':Departments})


def enrollment_form(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Order Confirmed")
            return redirect('form_page')
    else:
        form = EnrollmentForm()

    return render(request, 'form_page.html', {'form': form})



def success(request):
    return render(request, 'success.html')


from django.http import HttpResponse, JsonResponse


def get_Courses(request, department_id):
    courses = Course.objects.filter(department_id=department_id)
    c_list = [{"id": c.id, "name": c.name} for c in courses]
    return JsonResponse(c_list, safe=False)