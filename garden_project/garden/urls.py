from django.urls import path
from . import views
from .views import login_view


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

    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/create/', views.UserCreate.as_view(), name='user_create'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('users/<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', views.UserDelete.as_view(), name='user_delete'),
    path('register/', views.register_view, name='register'),
    path('login/', login_view, name='login'),
   
    
]
