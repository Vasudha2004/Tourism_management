from django.shortcuts import render

# Create your views here.

''' /loginmodule/views.py '''

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from loginmodule.models import Package,Category,Subcategory


def home(request):
	c={} 
	c.update(csrf(request))
	request.session['temp']="xyz"
	c['packs'] = Package.objects.all()
	return render(request,'home.html',c)

def contact_us(request):
	return render(request,'contact_us.html')

def login(request):
		c={}
		c.update(csrf(request))
		return render(request,'login.html',c)

def auth_view(request):
	username = request.POST.get('username','')
	userid=request.POST.get('userid','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username,user_id=userid, password=password)
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/BookTicketApp/book_ticket/')
	else:
		return render(request,'login.html',{"error":"Username or Password Invalid"})

def logout(request):
	auth.logout(request)
	return render(request, 'logout.html')

def aboutus(request):
	request.session['temp'] = "xyz"
	return render(request,'about_us.html')

def suggestions(request):
	c={} 
	c.update(csrf(request))
	request.session['temp']="xyz"
	c['cat']=Category.objects.all()
	return render(request,'suggestions.html',c)

def family(request):
	c={} 
	c.update(csrf(request))
	request.session['temp']="xyz"
	c['cat']=Subcategory.objects.filter(cat=1)
	return render(request,'family.html',c)

def religion(request):
	c={} 
	c.update(csrf(request))
	request.session['temp']="xyz"
	c['cat']=Subcategory.objects.filter(cat=2)
	return render(request,'religion.html',c)

def adventure(request):
	c={} 
	c.update(csrf(request))
	request.session['temp']="xyz"
	c['cat']=Subcategory.objects.filter(cat=3)
	return render(request,'adventure.html',c)

def special(request):
	c={} 
	c.update(csrf(request))
	request.session['temp']="xyz"
	c['cat']=Subcategory.objects.filter(cat=4)
	return render(request,'special.html',c)

def park(request):
	c={} 
	c.update(csrf(request))
	request.session['temp']="xyz"
	c['cat']=Subcategory.objects.filter(cat=5)
	return render(request,'park.html',c)

def friend(request):
	c={} 
	c.update(csrf(request))
	request.session['temp']="xyz"
	c['cat']=Subcategory.objects.filter(cat=6)
	return render(request,'friend.html',c)

