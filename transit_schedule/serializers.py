from rest_framework import serializers

class TransitDetailsRequestSerializer(serializers.Serializer):
    origin_station_id = serializers.CharField(max_length=100)
    coordinates = serializers.DictField(
        child=serializers.CharField(max_length=50),
        required=False
    )
    destination_station_id = serializers.CharField(max_length=100)

    def validate(self, data):
        if not data.get("origin_station_id") or not data.get("destination_station_id"):
            raise serializers.ValidationError("Origin and destination station IDs are required.")
        return data
