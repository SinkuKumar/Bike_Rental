from django.urls import path
from .views import booking_list


urlpatterns = [
    path('bookings/', booking_list, name='booking_list'),
]
