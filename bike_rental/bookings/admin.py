from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'bike', 'user', 'start_date', 'end_date', 'created_at')
    list_filter = ('start_date', 'end_date', 'created_at')
    search_fields = ('bike__name', 'user__username', 'user__email')
    ordering = ('-created_at',)
