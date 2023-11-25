from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    """
    Serializer class for converting Car model instances into JSON format and vice versa.
    Provides validation and deserialization of input data, and serialization of validated data into JSON.

    Example Usage:
    car = Car(name="Toyota Camry", price=25000, year=2020, origin="Japan", registration_date="2020-01-01", technical_inspection=True, first_hand=True, mileage=5000, fuel_type="Petrol", transmission="Automatic", num_doors=4, num_seats=5, power="150hp", co2_emission=120.5, length=4.8, trunk_volume=500, critair_rating=2, combined_consumption="7.5L/100km")
    serializer = CarSerializer(car)
    json_data = serializer.data
    print(json_data)
    deserialized_car = CarSerializer(data=json_data)
    if deserialized_car.is_valid():
        car_instance = deserialized_car.save()
        print(car_instance)

    Fields:
    - name: CharField representing the name of the car.
    - price: CharField representing the price of the car.
    - year: CharField representing the year of the car.
    - origin: CharField representing the origin of the car.
    - registration_date: CharField representing the registration date of the car.
    - technical_inspection: CharField representing whether the car has passed the technical inspection.
    - first_hand: CharField representing whether the car is a first-hand car.
    - mileage: CharField representing the mileage of the car.
    - fuel_type: CharField representing the fuel type of the car.
    - transmission: CharField representing the transmission type of the car.
    - num_doors: CharField representing the number of doors of the car.
    - num_seats: CharField representing the number of seats of the car.
    - power: CharField representing the power of the car.
    - co2_emission: CharField representing the CO2 emission of the car.
    - trunk_volume: CharField representing the trunk volume of the car.
    - length: CharField representing the length of the car.
    - critair_rating: CharField representing the Crit'Air rating of the car.
    - combined_consumption: CharField representing the combined fuel consumption of the car.
    """

    class Meta:
        model = Car
        fields = [
            "name",
            "price",
            "year",
            "origin",
            "registration_date",
            "technical_inspection",
            "first_hand",
            "mileage",
            "fuel_type",
            "transmission",
            "num_doors",
            "num_seats",
            "power",
            "co2_emission",
            "trunk_volume",
            "length",
            "critair_rating",
            "combined_consumption",
        ]


class UserInputSerializer(serializers.Serializer):
    name = serializers.CharField(allow_blank=True, allow_null=True)
    year = serializers.IntegerField(allow_null=True)
    origin = serializers.BooleanField(allow_null=True)
    technical_inspection = serializers.BooleanField(allow_null=True)
    first_hand = serializers.BooleanField(allow_null=True)
    mileage = serializers.FloatField(allow_null=True)
    fuel_type = serializers.CharField(allow_blank=True, allow_null=True)
    transmission = serializers.CharField(allow_blank=True, allow_null=True)
    num_doors = serializers.IntegerField(allow_null=True)
    num_seats = serializers.IntegerField(allow_null=True)
    power = serializers.IntegerField(allow_null=True)
    co2_emission = serializers.FloatField(allow_null=True)
    length = serializers.FloatField(allow_null=True)
    critair_rating = serializers.IntegerField(allow_null=True)
    combined_consumption = serializers.FloatField(allow_null=True)


class CarNameSerializer(serializers.Serializer):
    name = serializers.CharField()

    class Meta:
        fields = ["name"]
