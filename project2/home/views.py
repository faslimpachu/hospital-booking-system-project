from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Departments,Doctors,Booking,Signup
from .forms import BookingForm,LoginForm,SignupForm
from django.contrib import messages
from django.contrib.auth import logout as logouts





# Create your views here.
def hello(request):
    return HttpResponse("hello welcometo django home")

def login (request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']
            user = Signup.objects.get(Email=email)
            if not user:
                messages.warning(request, 'Email does not exist')
                return redirect('/login/')
            elif password != user.Password:
                messages.warning(request, 'Password not match')
                return redirect('/login/')
            else:
                messages.success(request, 'Login success')
                print("User ID:", user.id)
                return redirect('/home/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def about (request):
    return render(request,'about.html')

def doctors (request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }

    return render(request,'doctors.html',dict_docs)

def booking (request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'success.html')

    form=BookingForm()
    dict_form={
        'form': form
    }
    
    return render(request,'booking.html',dict_form)



def department (request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)


def index(request):
    return render(request,'index.html')
    

    

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['ConfirmPassword']

            user=Signup.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,'mail alredy exists')
                return redirect('/signup')
            elif password!=confirmpassword:
                messages.warning(request='password not match')
                return redirect('/signup')
            else:
                tab=Signup(Name=name,Age=age,Place=place,Email=email,Password=password)
                tab.save()
                messages.success(request,'data saved')
                return redirect('/login/')
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})

   

def logout(request):
    logouts(request)
    messages.success(request,'Logout success')
    return redirect('/')


def home(request):
    return render(request, 'home.html')

def mybooking(request):
    booking= Booking.objects.all()
    d = {'booking': booking}
    return render(request,'mybooking.html',d)

def tandc(request):
    return render(request,'tandc.html')