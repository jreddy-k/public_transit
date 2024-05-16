from django.urls import path
from .views import get_transit_details
urlpatterns = [
    path('get-transit-details/', get_transit_details),
]