from django.shortcuts import render
from .models import Info

# Create your views here.



def savestudentinfo(request):
    if request.method == "POST":
        if request.POST.get('studname') and request.POST.get('momname') and request.POST.get('dob') and request.POST.get('phonum') and request.POST.get('Gender'):
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
                return render(request,'info.html')
    
        
