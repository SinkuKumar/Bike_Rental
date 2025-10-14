from django.db import models


class Bike(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=100)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.model})"


class BikePhoto(models.Model):
    bike = models.ForeignKey(Bike, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/bike_photos/')

    def __str__(self):
        return f"Photo of {self.bike.name}"