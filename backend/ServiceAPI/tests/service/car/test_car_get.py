from django.test import TestCase
from ServiceAPI.models.car import Car
from ServiceAPI.service.car_service import CarService
from datetime import datetime


class GetTestCase(TestCase):
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

    def test_get_valid(self):
        dacia_logan = CarService.get(1)

        self.assertEqual(dacia_logan, Car.objects.get(pk=1))

    def test_get_invalid(self):
        returned_from_service = True
        returned_from_django = True

        try:
            car_from_service = CarService.get(24)
        except Car.DoesNotExist as e:
            returned_from_service = False

        try:
            car_from_django = Car.objects.get(pk=24)
        except Car.DoesNotExist as e:
            returned_from_django = False

        self.assertEqual(returned_from_service, returned_from_django)
