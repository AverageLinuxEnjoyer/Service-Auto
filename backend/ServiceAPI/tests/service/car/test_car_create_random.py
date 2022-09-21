from django.test import TestCase
from ServiceAPI.models.car import Car
from ServiceAPI.service.car_service import CarService
from datetime import datetime


class CreateRandomTestCase(TestCase):
    def setUp(self):
        Car.objects.create(
            model="Dacia Logan",
            acquisition_date=datetime(year=2011, month=4, day=26),
            kilometers=154900,
            warranty=False
        )

    def test_create_random(self):
        created_cars = CarService.createRandom(6, undoredo=False)
        total_cars_num = len(created_cars) + 1

        self.assertEqual(len(created_cars), 6)
        self.assertEqual(total_cars_num, len(Car.objects.all()))
