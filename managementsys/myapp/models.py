from django.db import models

# Create your models here.
class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    # This is a string representation of the tour
    def __str__(self):
        return (
            f"Tour #{self.id}: from {self.origin_country} to {self.destination_country}, "
            f"{self.number_of_nights} night(s), price: ${self.price}"
        )