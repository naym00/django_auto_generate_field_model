from django.contrib import admin
from myapp.models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'booking_id', 'booking_name']