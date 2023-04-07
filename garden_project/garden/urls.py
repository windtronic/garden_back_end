from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.PlantList.as_view(), name='plant_list'),
    path('plants/', views.PlantList.as_view(), name='plant_list'),
    path('plant_listings/', views.PlantListingList.as_view(), name='plant_listing_list'),
    path('calendars/', views.CalendarList.as_view(), name='calendar_list'),
    path('plants/<int:pk>/', views.PlantDetail.as_view(), name='plantdetail'),
    path('plant_listings/<int:pk>/', views.PlantListingDetail.as_view(), name='plant_listing_detail'),
    path('calenders/<int:pk>/', views.CalenderDetail.as_view(), name='calender_detail'),
    path('plants/<int:venue_pk>/plant_listings', views.PlantListingList.as_view(), name='plant_listing_list'),
    # path('venues/<int:venue_pk>/events/<int:event_pk>/', views.EventVenueDetail.as_view(), name='event_venue_detail'),
    # path('create-ticket-detail/', views.TicketCreateView.as_view(), name='create_ticket_detail')

]