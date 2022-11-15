
from django.urls import path, include
from . import views

urlpatterns=[
	path('SignupApp/signup/', views.signup, name = 'signup'),
    path('SignupApp/adduserinfo/', views.adduserinfo, name = 'userinfo'),
]