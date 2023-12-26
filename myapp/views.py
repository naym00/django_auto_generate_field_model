from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from myapp.models import *
from myapp.serializer import *
from django.core.paginator import Paginator

# http://127.0.0.1:8000/myapp/?page=4
@api_view(['GET'])
def index(request):
    bookings = Booking.objects.all()
    paginator = Paginator(bookings, 3)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    bookingserializer = BookingSerializer(page_obj, many=True)
    return Response(bookingserializer.data, status=status.HTTP_200_OK)
