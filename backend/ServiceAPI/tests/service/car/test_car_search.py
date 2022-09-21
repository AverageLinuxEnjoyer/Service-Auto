from django.test import TestCase
from ServiceAPI.models.car import Car
from ServiceAPI.service.car_service import CarService
from datetime import datetime


class SearchTestCase(TestCase):
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
            kilometers=48526,
            warranty=True
        )

    def test_search_valid(self):
        cars = CarService.search("26")

        self.assertQuerysetEqual(cars, Car.objects.all(), ordered=False)

    def test_search_no_results(self):
        cars = CarService.search("laborator ubb")

        self.assertNotEqual(cars, Car.objects.all())
        self.assertNotEqual(len(cars), len(Car.objects.all()))
