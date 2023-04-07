from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import PlantSerializer, PlantListingSerializer, CalendarSerializer
from .models import Plant, PlantListing, Calendar

class PlantList(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class PlantCreate(generics.CreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantUpdate(generics.UpdateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class PlantDelete(generics.DestroyAPIView):
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
