''' /BookTicketApp/views.py '''
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from loginmodule.models import Booking,Package
from loginmodule.models import Users
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils.crypto import get_random_string
from django.utils.timezone import datetime
@login_required
def book_ticket(request):
	c={} 
	c.update(csrf(request))
	request.session['temp']="xyz"
	request.session['full_name']=request.user.username
	c['packs'] = Package.objects.all()
	c['randomid']=get_random_string(length=6)
	return render(request,'book_ticket.html',c)
@login_required
def bookingdataadd(request):
    bookingid=request.POST.get('bookingid','')
    source1=request.POST.get('source','')
    destination1=request.POST.get('destination','')
    package=request.POST.get('package','')
    frdate=request.POST.get('fromdate','')
    todate=request.POST.get('todate','')

    #no_of_person=request.POST.get('person','')
	#amt=Package.objects.get(pname=package1).amount
    total_amount=Package.objects.get(pack_name=package).pack_price
    request.session['total_amount']=total_amount
    s=Booking(booking_id=bookingid,
				 pack_id=Package.objects.get(pack_name=package).pack_id,
				 user=Users.objects.get(name=request.user.username),
                 fromdate=frdate,
                 todate=todate
                 
                 )
    if(source1 != destination1):
        s.save()
        request.session['package']=package
        request.session['fromdate']=frdate
        request.session['todate']=todate

        return HttpResponseRedirect('/PaymentApp/CalculateAmount/')
    else:
        request.session['error3']="Source and Destination cannot be same"
        return HttpResponseRedirect('/BookTicketApp/book_ticket/')

	
@login_required
def booking_history(request):
	request.session['temp']="abc"
	c={}
	c['today']=datetime.today().date()
	c['bookings'] = Booking.objects.all()
	return render(request,'booking_history.html',c)
def delete(request):
	Booking.objects.filter(booking_id=request.POST.get('cancel')).delete()
	return HttpResponseRedirect('/BookTicketApp/booking_history/')
@login_required
def feedback(request):
	return render(request,'feedback.html')
def addfeedback(request):
	feedback=request.POST.get('feedback','')
	f=feedback(user_id=Users.objects.get(user_id=request.user),feedback=feedback)
	f.save()
	return render(request,'home.html')