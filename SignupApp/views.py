from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from loginmodule.models import Users
from django.contrib.auth.models import User
# Create your views here.


def signup(request):
    c={}
    c.update(csrf(request))
    return render(request,'signup.html',c)

def adduserinfo(request):
	uname=request.POST.get('username','')
	uid=request.POST.get('user_id','')
	pwd=request.POST.get('password','')
	cpwd=request.POST.get('cpassword','')
	emailid=request.POST.get('emailid','')
	mno=request.POST.get('mobileno','')
	if(pwd==cpwd):
		if(len(pwd)>=8):
			u=User.objects.create_user(username=uname,password=pwd,email=emailid)
			print(u)
			u.Users = Users(user_id=uid,name=uname,email_id=emailid,mob_num=mno,pswd=pwd)
			u.Users.save()
			u.save()
			return HttpResponseRedirect('/loginmodule/login/')
		else:
			return render(request,'signup.html',{"error1":"password length is lessthan 8"})
	else:
		return render(request,'signup.html',{"error2":"password doesn't match enter again"})