from django.test import TestCase
from rest_framework.test import APIClient
from .serializers import TransitDetailsRequestSerializer

class TransitDetailsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_transit_details_valid_request(self):
        request_data = {
            "origin_station_id": "1",
            "destination_station_id": "10",
        }
        serializer = TransitDetailsRequestSerializer(data=request_data)
        self.assertTrue(serializer.is_valid())

        response = self.client.post('/get-transit-details/', data=request_data)
        self.assertEqual(response.status_code, 200)

        expected_keys = ["transit_mode", "eta_origin", "eta_destination"]
        for item in response.data:
            for key in expected_keys:
                self.assertIn(key, item)

    def test_get_transit_details_invalid_request(self):
        invalid_request_data = {
            "destination_station_id": "10",
        }
        response = self.client.post('/get-transit-details/', data=invalid_request_data)

        self.assertEqual(response.status_code, 400)
