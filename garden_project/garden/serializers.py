from rest_framework import serializers
from .models import Plant, PlantListing, Calendar, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'address', 'email', 'password']


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'user', 'name']


class PlantListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantListing
        fields = ['id', 'plant', 'name', 'row_spacing', 'seed_depth', 'sunlight_needs', 'season', 'water_needs', 'frost_tolerance', 'germination_time', 'harvest_times', 'grow_from_seed', 'grow_from_transplant', 'plant_needs_fertilization', 'date_to_plant']


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ['id', 'user', 'frost_dates', 'plant_dates', 'harvest_times', 'fertilize_dates', 'comments']
