'''/PaymentApp/urls.py'''

from django.urls import path, include
from . import views

urlpatterns=[
	path('PaymentApp/CalculateAmount/',views.CalculateAmount, name = 'CalculateAmount'),
	path('PaymentApp/makepayment/', views.makepayment,name = 'makepayment'),
	path('PaymentApp/bill/', views.bill,name = 'bill'),
]