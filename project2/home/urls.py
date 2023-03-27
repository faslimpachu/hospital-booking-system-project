
from django.urls import path
from . import views

urlpatterns = [
    path('hello/',views.home,name='home' ),
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('doctors/',views.doctors,name='doctors'),
    path('booking/',views.booking,name='booking'),
    path('department/',views.department,name='department'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('mybooking/',views.mybooking,name='mybooking'),
    path('home/', views.home, name='home'),
    path('tandc/', views.tandc, name='tandc'),




    
]