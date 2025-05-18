from django.shortcuts import render, redirect
from .models import Service, Booking, PhotoGallery
from .forms import BookingForm, RegistrationForm,ContactForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .serializers import ServiceSerializer,PhotoGallerySerializer,BookingSerializer



# Create your views here.

def home(request):
    return render(request, 'main/home.html')


def services(request):
    services = Service.objects.all()
    return render(request, 'main/services.html', {'services': services})


def gallery(request):
    photos = PhotoGallery.objects.all()
    return render(request, 'main/gallery.html', {'photos': photos})


def book_photographer(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = BookingForm()
            return render(request, 'main/booking.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})


@login_required
def book_photographer(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'main/booking.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('home')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html',{'form':form})

# api

class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class BookingListAPIView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class PhotoGalleryListAPIView(generics.ListAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer
