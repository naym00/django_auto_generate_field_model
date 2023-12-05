from django.db import models

import datetime

def increment_booking_number():
    last_booking = Booking.objects.all().order_by('id').last()
    if not last_booking:
        return 'RNH' + str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + '0000'
    booking_id = last_booking.booking_id
    booking_int = int(booking_id[9:13])
    new_booking_int = booking_int + 1
    new_booking_id = 'RNH' + str(str(datetime.date.today().year)) + str(datetime.date.today().month).zfill(2) + str(new_booking_int).zfill(4)
    return new_booking_id

class Booking(models.Model):
    booking_name = models.CharField(max_length = 20, blank=True, null=True)
    booking_id = models.CharField(max_length = 20, default = increment_booking_number, editable=False)
    
    def __str__(self):
        return f'{self.booking_id} -- {self.booking_name}'