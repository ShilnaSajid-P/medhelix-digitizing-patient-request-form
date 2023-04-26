from django.shortcuts import render, redirect, get_object_or_404
from .forms import Userform,RegistrationForm,LoginForm
from .models import Userr
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import View
import uuid
import datetime
from django.core.files.base import ContentFile
from django.shortcuts import render
from django.http import HttpResponse
# from .forms import VideoStreamingForm
# from .models import VideoStreaming
import base64





# Create your views here.

def signin_required(fn):
    def wrapper(request,*args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"signin required")
            return redirect("signin")
        else:
            return fn(request, *args, **kwargs)
    return wrapper

@signin_required


def add(request):
    if request.method == 'POST':
        form = Userform(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            image = form.cleaned_data['image']
            file_ext = image.name.split('.')[-1]
            now = datetime.datetime.now()
            date_string = now.strftime('%Y-%m-%d')
            serial_no = str(user.serial_no)
            filename = date_string + 'MEDHELIX' + serial_no + '.' + file_ext
            user.image.save(filename, image)
            user.save()
            return render(request, 'success.html')
    else:
        form = Userform()
    return render(request, 'base.html', {'form': form})



@signin_required
def search_prescription(request):
    if request.method == 'POST':
        prescription_id = request.POST.get('prescription_id')
        prescription_date = request.POST.get('date')
        try:
            if prescription_id:
                prescription = Userr.objects.filter(serial_no=prescription_id).first()
                if prescription:
                    if prescription.image:
                        # Check if the image field is not empty
                        return render(request, 'detail.html', {'prescription': prescription})
                    else:
                        messages.error(request, 'No image found for this prescription.')
                else:
                    messages.error(request, 'Prescription not found.')
            elif prescription_date:
                prescriptions = Userr.objects.filter(date=prescription_date)
                if prescriptions:
                    return render(request, 'detail1.html', {'prescriptions': prescriptions, 'prescription_date': prescription_date})
                else:
                    messages.error(request, 'No prescriptions found for this date.')
            else:
                messages.error(request, 'Please enter a prescription ID or date.')
        except Userr.DoesNotExist:
            messages.error(request, 'Prescription not found.')
    return render(request, 'search.html')



#new

class RegistrationView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            User.objects.create_user(**form.cleaned_data)
            # messages.success(request,"Registration Successful")
            return redirect("signin")
        else:
            messages.error(request,"Failed to Register")
            return redirect("register")

class LoginView(View):    
    def get(self,request,*args, **kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                return render(request,"base.html")
            else:
                print("login failed")
                messages.error(request,"invalid Credentials")
                return redirect("signin")
            
@signin_required
def home(request):
    # Your view logic here
    return render(request, 'home.html')

@signin_required
def signout(request,*args, **kwargs):
    logout(request)
    return redirect("signin")
