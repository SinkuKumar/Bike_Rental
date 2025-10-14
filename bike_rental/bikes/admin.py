from django.contrib import admin
from .models import Bike, BikePhoto

# Inline admin for photos
class BikePhotoInline(admin.TabularInline):  # or admin.StackedInline for a larger form layout
    model = BikePhoto
    extra = 1  # how many empty forms to show for adding new photos

# Admin for Bike model
@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    inlines = [BikePhotoInline]
    list_display = ('id', 'name', 'model', 'price_per_hour', 'price_per_day')  # adjust as per your Bike model

# Optional: still register BikePhoto separately if you want to access it directly too
@admin.register(BikePhoto)
class BikePhotoAdmin(admin.ModelAdmin):
    list_display = ('bike', 'image')