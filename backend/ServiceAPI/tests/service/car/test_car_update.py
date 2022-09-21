from django.test import TestCase
from ServiceAPI.models.car import Car
from ServiceAPI.service.car_service import CarService
from datetime import datetime


class UpdateTestCase(TestCase):
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

    def test_update(self):
        dacia_spring = CarService.update(
            Car(
                model="Dacia Spring",
                acquisition_date=datetime(year=2021, month=10, day=3),
                kilometers=4096,
                warranty=True
            ),
            1,
            undoredo=False
        )

        self.assertEqual(dacia_spring, Car.objects.get(pk=1))
