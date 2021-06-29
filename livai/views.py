from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Booking
from rest_framework import serializers, viewsets
from .serializers import BookingSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

#from .models import Info

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method=="POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['uname']
        email = request.POST['email']
        password1 = request.POST['psw1']
        password2 = request.POST['psw2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email exists")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return render(request, "login.html")
        else:
            print("password not matching")
            return redirect('register')

    else:
        return render(request,'register.html')


    
def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return render(request,'booking.html')
        else:
            messages.info(request,'User not authorized!')
            return redirect('login')

    else:
        return render(request, 'login.html')


def book(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('movie') and request.POST.get('persons') and request.POST.get('date') and request.POST.get('time') and request.POST.get('seatnames'):
            save = Booking()
            save.name = request.POST.get('name')
            x = request.POST.get('movie').split("/")
            picture = x[0]
            save.movie = picture
            cost = int(x[1])
            tickets = int(request.POST.get("persons"))
            totalprice = cost*tickets
            save.price = totalprice
            save.persons = request.POST.get('persons')
            Date = request.POST.get('date')
            save.date = Date
            Time = request.POST.get('time')
            save.time = Time
            save.seats = request.POST.get('seatnames')
            save.save()
            return render(request, 'confirm.html', {'price':totalprice, 'movie':picture, 'date':Date, 'time':Time})
    else:
        return render(request,'booking.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]





"""def save(request):
        if request.method == "POST":
                if request.POST.get('studname') and request.POST.get('momname') and request.POST.get('dob') and request.POST.get('phonum') and request.POST.get('Gender'):
                        info=Info()
                        info.student_name= request.POST.get('studname')
                        info.mother_name = request.POST.get('momname')
                        info.Dob = request.POST.get('dob')
                        info.contact_number = request.POST.get('phonum')
                        info.gender= request.POST.get('Gender')
                        info.save()
                        messages.success(request,"SAVED WOOHOO")
                        return render(request,'listing.html')  
        else:
                return render(request, "info.html")"""

'''def createpost(request):
    if request.method == "POST":
        if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request,'practice.html')  

        else:
                return render(request,'practice.html')'''

'''def savestudentinfo(request):
    if request.method == "POST":
        if request.POST.get('First_name') and request.POST.get('Last_name'):
                info=Info()
                info.student_name= request.POST.get('studname')
                info.mother_name = request.POST.get('momname')
                info.Dob = request.POST.get('dob')
                info.contact_number = request.POST.get('phonum')
                info.gender= request.POST.get('Gender')
                info.email_field= request.POST.get('email')
                info.address = request.POST.get('Address')
                info.pin_code= request.POST.get('pincode')
                info.school = request.POST.get('schoolname')
                info.board = request.POST.get('board')
                info.tenth_cgpa = request.POST.get('tenth')
                info.twelth_perc = request.POST.get('twelth')
                info.college = request.POST.get('college')
                info.batch = request.POST.get('batch')
                info.course = request.POST.get('course')
                info.stream = request.POST.get('stream')
                info.department = request.POST.get('dept')
                info.mentor_name = request.POST.get('mentor')
                info.stipend = request.POST.get('salary')
                info.duration = request.POST.get('duration')
                info.save()
                
                return render(request,'listing.html')  

        else:
                return render(request,'info.html')'''

'''if request.POST.get('Male'):
                    info.Gender = request.POST.get('Male')
                elif request.POST.get('Female'):
                    info.Gender = request.POST.get('Female')
                elif request.POST.get('Other'):
                    info.Gender = request.POST.get('Other')
                info.Gender = request.POST.get('Male' or 'Female'or 'Other')'''

