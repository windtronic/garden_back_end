from django.contrib.auth import get_user_model, authenticate, login
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .serializers import (
    UserSerializer,
    CalendarSerializer,
    PlantSerializer,
    PlantListingSerializer
)
from .models import User, Calendar, Plant, PlantListing


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        for user in queryset:
            print(user.name)
        return queryset


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


@api_view(['POST'])
@csrf_exempt
@permission_classes([AllowAny])
def register_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        address = request.data.get('address')
        User = get_user_model()
        user = User.objects.create_user(username=username, email=email, password=password)
        user.address = address
        user.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

@api_view(['POST'])
@csrf_exempt
@permission_classes([AllowAny])
def login_view(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return JsonResponse({'success': True, 'message': 'Login successful'})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid email or password'})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Invalid email or password'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})
