from django.test import TestCase
from django.urls import resolve


class CarRoutesTestCase(TestCase):
    def test_car_list_url(self):
        resolver = resolve('/car/list/')
        self.assertEqual(resolver.view_name, "car-list")

    def test_car_list_by_workmanship_url(self):
        resolver = resolve('/car/listByWorkmanship/')
        self.assertEqual(resolver.view_name,
                         "car-list-decreasing-by-workmanship")

    def test_car_detail_url(self):
        resolver = resolve('/car/detail/5/')
        self.assertEqual(resolver.view_name, "car-detail")

    def test_car_create_url(self):
        resolver = resolve('/car/create/')
        self.assertEqual(resolver.view_name, "car-create")

    def test_car_create_random_url(self):
        resolver = resolve('/car/random/5/')
        self.assertEqual(resolver.view_name, "car-create-random")

    def test_car_update_url(self):
        resolver = resolve('/car/update/5/')
        self.assertEqual(resolver.view_name, "car-update")

    def test_car_renew_warranty_url(self):
        resolver = resolve('/car/renewWarranty/')
        self.assertEqual(resolver.view_name, "car-renew-warranty")

    def test_car_delete_url(self):
        resolver = resolve('/car/delete/5/')
        self.assertEqual(resolver.view_name, "car-delete")
