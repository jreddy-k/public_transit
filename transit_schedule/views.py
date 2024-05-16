from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TransitDetailsRequestSerializer
from rest_framework import status
import json
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(request_body=TransitDetailsRequestSerializer, methods=['POST'])
@api_view(['POST'])
def get_transit_details(request):
    serializer = TransitDetailsRequestSerializer(data=request.data)
    if serializer.is_valid():
        with open("transit_schedule/schedules.json") as json_file:
            schedule_data = json.load(json_file)
            timings = [{"transit_mode" : item.get("transit_mode"), "eta_origin": item.get("eta_origin"), "eta_destination":item.get("eta_destination")} for item in schedule_data if item.get("origin_station_id") == serializer.data.get("origin_station_id") and item.get("destination_station_id") == serializer.data.get("destination_station_id")]
        
        return Response(timings, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

