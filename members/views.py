from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from datetime import datetime
#from django.http import HttpResponse
#from django.template import loader
#from .models import Member
#def members(request):
    #template=loader.get_template('registration.html')
    #return HttpResponse(template.render())
# Create your views here.
def HomePage(request):
    #context={'name':'Vijay','age':20}
    #return HttpResponse('home page')
    return render(request,'home.html')
def SignupPage(request):
    if (request.method=='POST'):
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Confirm password doesn't match")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
            return HttpResponse("User has been created Sucessfully!!!")
    return render(request,'signup.html')
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
       # print(email,password)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            return HttpResponse("Username or Password is incorrect!")  
    return render (request,'Login.html')

#def LandingPage(request):
 #   return render(request,'landingpage.html')
def Stage1(request):
    return render(request,'stage1.html')
def Stage2(request):
    return render(request,'stage2.html')
def Stage3(request):
    return render(request,'stage3.html')
def Stage4(request):
    return render(request,'stage4.html')
def Stage5(request):
    return render(request,'stage5.html')
def Profile(request):
    #user = request.user
    # Retrieve the user's data from the Django database
    # You can access the user's attributes such as email, first_name, last_name etc from user object.
    data = {
        'name': request.user.username,
        'email': request.user.email,
        # Add more data here
    }
    return render(request, 'profile.html', {'data': data})
def Logout(request):
    return render(request,'logout.html')
def Contact(request):
    return render(request,'contact.html')
def Treasure(request):
    return render(request,'treasure.html')