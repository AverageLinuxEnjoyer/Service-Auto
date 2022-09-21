from django.test import TestCase
from ServiceAPI.models.car import Car
from ServiceAPI.service.car_service import CarService
from datetime import datetime


class RenewWarrantyTestCase(TestCase):
    def setUp(self):
        Car.objects.create(
            model="Dacia Logan",
            acquisition_date=datetime(year=2011, month=4, day=26),
            kilometers=154900,
            warranty=False
        )

        Car.objects.create(
            model="Dacia Duster",
            acquisition_date=datetime(year=2019, month=9, day=30),
            kilometers=48500,
            warranty=False
        )

    def test_renew_warranty(self):
        dacia_logan_warranty = Car.objects.get(pk=1).warranty
        dacia_duster_warranty = Car.objects.get(pk=2).warranty

        CarService.renewWarranty(undoredo=False)

        new_dacia_logan_warranty = Car.objects.get(pk=1).warranty
        new_dacia_duster_warranty = Car.objects.get(pk=2).warranty

        self.assertEqual(dacia_logan_warranty, new_dacia_logan_warranty)
        self.assertNotEqual(dacia_duster_warranty, new_dacia_duster_warranty)
