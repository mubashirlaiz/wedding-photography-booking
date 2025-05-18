from django.urls import path
from .import views
from .views import ServiceListAPIView,BookingListAPIView,PhotoGalleryListAPIView,contact

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('book/', views.book_photographer, name='book'),
    path('register/', views.register, name='register'),
    path('contact/',contact,name='contact'),
    path('api/services/',ServiceListAPIView.as_view(),name='service-list'),
    path('api/services/',BookingListAPIView.as_view(),name='booking-list'),
    path('api/services/',PhotoGalleryListAPIView.as_view(),name='gallery-list'),
]
