from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('contact_us/',views.contact_us, name= 'contactus'),
    path('loginmodule/login/', views.login, name= 'login'),
    path('loginmodule/logout/', views.logout, name = 'logout'),
    path('loginmodule/auth/', views.auth_view, name = 'auth'),
    path('loginmodule/aboutus/', views.aboutus, name = 'aboutus'),
    path('loginmodule/suggestions/', views.suggestions, name = 'suggestions'),
    path('loginmodule/suggestions/fam', views.family, name = 'family'),
    path('loginmodule/suggestions/rel', views.religion, name = 'religion'),
    path('loginmodule/suggestions/adv', views.adventure, name = 'adventure'),
    path('loginmodule/suggestions/spl', views.special, name = 'special'),
    path('loginmodule/suggestions/nat', views.park, name = 'park'),
    path('loginmodule/suggestions/frn', views.friend, name = 'friend'),
]