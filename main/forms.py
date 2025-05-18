from django import forms
from .models import Booking,Contact,Service
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'service', 'date', 'time', 'notes']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email','message']
                  
