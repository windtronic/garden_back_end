from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('plants/', views.PlantList.as_view(), name='plant_list'),
    path('plants/create/', views.PlantCreate.as_view(), name='plant_create'),
    path('plants/<int:pk>/', views.PlantDetail.as_view(), name='plant_detail'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plant_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plant_delete'),

    path('plant_listings/', views.PlantListingList.as_view(), name='plant_listing_list'),
    path('plant_listings/<int:pk>/', views.PlantListingDetail.as_view(), name='plant_listing_detail'),

    path('calendars/', views.CalendarList.as_view(), name='calendar_list'),
    path('calendars/<int:pk>/', views.CalendarDetail.as_view(), name='calendar_detail'),
]
