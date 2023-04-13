from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, CalendarSerializer, PlantSerializer, PlantListingSerializer
from .models import User, Calendar, Plant, PlantListing

User = get_user_model()

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CalendarList(generics.ListCreateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

class CalendarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

class PlantList(generics.ListCreateAPIView):
    queryset = Plant.objects.order_by('name')
    serializer_class = PlantSerializer


class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

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

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        address = request.POST.get('address')
        user = User.objects.create_user(username, email, password)
        user.address = address
        user.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

