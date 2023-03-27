from django import forms
from .models import Booking,Signup

class DateInput(forms.DateInput):
    input_type='date'



class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields= '__all__'

        widgets = {
            'booking_date':DateInput(),
            'p_name':forms.TextInput(attrs={'class':'form-control', 'type':'text'}),
            'p_phone':forms.TextInput(attrs={'class':'form-control', 'type':'phone_number'}),
            'p_email':forms.EmailInput(attrs={'class':'form-control', 'type':'email'}),
           

           
            
        }

        labels={
            'p_name':'Patinet name',
            'p_phone':'Patinet phone',
            'p_email':'Patinet email',
            'doc_name':'Doctor Name',
            'booking_date':'Booking date',
            
           
        }
class SignupForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
       
        model=Signup
       
        fields='__all__'

        widgets={
             'Name':forms.TextInput(attrs={'class':'form-control', 'type':'text'}),
             'Age':forms.TextInput(attrs={'class':'form-control', 'type':'text'}),
             'Place':forms.TextInput(attrs={'class':'form-control', 'type':'text'}),
             'email':forms.EmailInput(attrs={'class':'form-control', 'type':'email'}),
             'password':forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}),
             'confirmpassowrd':forms.PasswordInput(attrs={'class':'form-control','type':'password'}),
               
                 
               
        }







class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput,max_length=8,min_length=2)
    class Meta():
        model=Signup
        fields=('Email','Password')

       