from django.shortcuts import render
from .models import Booking
from django.contrib.auth.decorators import login_required

@login_required
def booking_list(request):
    bookings = Booking.objects.order_by('-created_at')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})
