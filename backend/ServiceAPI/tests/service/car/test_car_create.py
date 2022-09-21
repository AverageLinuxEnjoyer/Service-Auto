from django.test import TestCase
from ServiceAPI.models.car import Car
from ServiceAPI.service.car_service import CarService
from datetime import datetime


class CreateTestCase(TestCase):
    def setUp(self):
        Car.objects.create(
            model="Dacia Logan",
            acquisition_date=datetime(year=2011, month=4, day=26),
            kilometers=154900,
            warranty=False
        )

        Car.objects.create(
            model="Dacia Duster",
            acquisition_date=datetime(year=2018, month=9, day=30),
            kilometers=48500,
            warranty=True
        )

    def test_create(self):
        dacia_spring = CarService.create(
            Car(
                model="Dacia Spring",
                acquisition_date=datetime(year=2020, month=9, day=30),
                kilometers=8500,
                warranty=True
            )
        )

        self.assertEqual(dacia_spring, Car.objects.get(pk=3))
