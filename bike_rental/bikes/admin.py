from django.contrib import admin
from .models import Bike, BikePhoto

# Inline admin for photos
class BikePhotoInline(admin.TabularInline):  # or admin.StackedInline for a larger form layout
    model = BikePhoto
    extra = 1  # how many empty forms to show for adding new photos

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    inlines = [BikePhotoInline]
    list_display = ('id', 'name', 'model', 'price_per_hour', 'price_per_day')
    search_fields = ('name', 'model', 'description')
    list_filter = ('model',)
    ordering = ('name',)


# @admin.register(BikePhoto)
# class BikePhotoAdmin(admin.ModelAdmin):
#     list_display = ('bike', 'image')
#     search_fields = ('bike__name',)
#     list_filter = ('bike__model',)
#     ordering = ('bike',)