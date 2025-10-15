from django.shortcuts import render
from .models import Bike

def bike_list(request):
    bikes = Bike.objects.prefetch_related('photos').all()
    return render(request, 'bikes/bike.html', {'bikes': bikes})

def bike_search(request):
    query = request.GET.get('q', '')
    bikes = Bike.objects.filter(name__icontains=query).prefetch_related('photos')
    return render(request, 'bikes/bike.html', {'bikes': bikes, 'query': query})