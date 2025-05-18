from django.contrib import admin
from .models import Service, Booking, PhotoGallery

# Register your models here.


# Register your models here
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Fields to display in the admin list view
    search_fields = ('name',)  # Enable search by name

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'date', 'time')  # Fields to display
    list_filter = ('date', 'service')  # Add filters for date and service
    search_fields = ('user_username', 'service_name')  # Enable search by username and service name

@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Fields to display
    search_fields = ('title',)  # Enable search by title