from django.db import models


class Booking(models.Model):
    bike = models.ForeignKey('bikes.Bike', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} by {self.user.username} for {self.bike.name}"