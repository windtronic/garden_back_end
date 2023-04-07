from rest_framework import generics
from .models import Plant, PlantListing, Calendar
from .serializers import PlantSerializer, PlantListingSerializer, CalendarSerializer

class PlantList(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantListingList(generics.ListCreateAPIView):
    queryset = PlantListing.objects.all()
    serializer_class = PlantListingSerializer

class PlantListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlantListing.objects.all()
    serializer_class = PlantListingSerializer

class CalendarList(generics.ListCreateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

class CalendarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
