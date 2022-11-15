''' /BookTicketApp/urls.py '''

from . import views
from django.urls import path

urlpatterns=[
	path('BookTicketApp/book_ticket/',views.book_ticket,name = 'book_ticket'),
	path('BookTicketApp/bookingdataadd/',views.bookingdataadd,name = 'bookingdataadd'),
	path('BookTicketApp/booking_history/',views.booking_history, name = 'booking_history'),
	path('BookTicketApp/delete/', views.delete,name = 'delete'),
	path('BookTicketApp/feedback/', views.feedback,name = 'feedback'),
    #path('BookTicketApp/addfeedback/',views.addfeedback, name = 'addfeedback'),

]