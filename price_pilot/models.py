from djongo import models


class Car(models.Model):
    """
    Represents a car object with information about the car's brand, model, year, kilometers, and number of seats.
    """

    _id = models.ObjectIdField(default=None)
    name = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=100, null=True)
    year = models.CharField(max_length=100, null=True)
    origin = models.CharField(max_length=100, null=True)
    registration_date = models.CharField(max_length=100, null=True)
    technical_inspection = models.CharField(max_length=100, null=True)
    first_hand = models.CharField(max_length=100, null=True)
    mileage = models.CharField(max_length=100, null=True)
    fuel_type = models.CharField(max_length=100, null=True)
    transmission = models.CharField(max_length=100, null=True)
    num_doors = models.CharField(max_length=100, null=True)
    num_seats = models.CharField(max_length=100, null=True)
    power = models.CharField(max_length=100, null=True)
    co2_emission = models.CharField(max_length=100, null=True)
    trunk_volume = models.CharField(max_length=100, null=True)
    length = models.CharField(max_length=100, null=True)
    critair_rating = models.CharField(max_length=100, null=True)
    combined_consumption = models.CharField(max_length=100, null=True)

    def __str__(self):
        """
        Returns a string representation of the car object, including the brand, model, and year.
        """
        return f"{self.name} - {self.year}"
