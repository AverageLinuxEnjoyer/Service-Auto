from django.test import TestCase
from ServiceAPI.models.car import Car
from ServiceAPI.service.car_service import CarService
from datetime import datetime


class DeleteTestCase(TestCase):
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

    def test_delete_valid(self):
        initial_car_count = len(Car.objects.all())

        CarService.delete(1, undoredo=False)

        new_car_count = len(Car.objects.all())

        self.assertEqual(new_car_count, 1)
        self.assertNotEqual(initial_car_count, new_car_count)

    def test_delete_invalid(self):
        initial_car_count = len(Car.objects.all())

        try:
            CarService.delete(5, undoredo=False)
        except Car.DoesNotExist as e:
            pass

        new_car_count = len(Car.objects.all())

        self.assertEqual(initial_car_count, new_car_count)
