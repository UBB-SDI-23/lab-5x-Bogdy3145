from rest_framework import status
from rest_framework.reverse import reverse

from django1.models import Cars
from django1.models import Brand
from rest_framework.test import APIClient

from django1.urls import urlpatterns

from django.test import TestCase
from django1.serializers import serializers, StatisticSerializer, StatisticFoundingSerializer


class statistics_testcase(TestCase):

    def setUp(self):
        brand1 = Brand.objects.create(
            name='brand1',
            founding_year=2000,
            owner_name="Bolo",
            rarity="common",
            hq_address="testadress"
        )
        brand2 = Brand.objects.create(
            name='brand2',
            founding_year=2010,
            owner_name="Bolo",
            rarity="common",
            hq_address="testadress"
        )

        Cars.objects.create(
            name=brand1,
            description='desc',
            engine="V6",
            type="common",
            year=2000,
            horsepower=100
        )
        Cars.objects.create(
            name=brand1,
            description='desc',
            engine="V12",
            type="common",
            year=2010,
            horsepower = 150
        )
        Cars.objects.create(
            name=brand2,
            description='desc',
            engine="V6",
            type="common",
            year=2000,
            horsepower = 200
        )

    def test_statistic(self):
        client = APIClient()
        url = reverse('stat')
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = [
            {
                "id": 1,
                "name": "brand1",
                "avg_production_year": 2005,
                "car_count": 2
            },
            {
                "id": 2,
                "name": "brand2",
                "avg_production_year": 2000,
                "car_count": 1
            }
        ]
        serializer = StatisticSerializer (expected_data, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_statistic2(self):
        client = APIClient()
        url = reverse('stat2')
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = [
            {
                "id": 2,
                "name": "brand2",
                "avg_hp": 200,
                "car_count": 1
            },
            {
                "id": 1,
                "name": "brand1",
                "avg_hp": 125,
                "car_count": 2
            }

        ]
        serializer = StatisticFoundingSerializer(expected_data, many=True)
        self.assertEqual(response.data, serializer.data)