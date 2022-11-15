''' /PaymentApp/views.py '''

from django.shortcuts import render
from django.template.context_processors import csrf
from loginmodule.models import Package,Booking
from django.contrib.auth.decorators import login_required
from loginmodule.models import Users
from loginmodule.models import Payment
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect
from django.utils.crypto import get_random_string

@login_required
def CalculateAmount(request):
    return render(request,'amount.html')

@login_required
def makepayment(request):
    c={}
    c.update(csrf(request))
    request.session['mode']=request.POST.get('mode','')
    return render(request,'payment_mode.html',c)

@login_required
def bill(request):
    c={}
    paymentid=get_random_string(length=6)
    mode=request.session.get('mode')
    amount=request.session.get('total_amount')
    p=Payment(payment_id=paymentid,amount=amount,mode=mode,user_id=Users.objects.get(name=request.user).user_id)
    p.save()
    return render(request,'bill.html',c)