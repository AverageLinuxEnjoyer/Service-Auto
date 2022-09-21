from django.test import TestCase
from django.urls import resolve


class CardRoutesTestCase(TestCase):
    def test_card_list_url(self):
        resolver = resolve('/card/list/')
        self.assertEqual(resolver.view_name, "card-list")

    def test_car_list_by_workmanship_url(self):
        resolver = resolve('/card/listByDiscount/')
        self.assertEqual(resolver.view_name,
                         "card-list-decreasing-by-discount")

    def test_card_detail_url(self):
        resolver = resolve('/card/detail/5/')
        self.assertEqual(resolver.view_name, "card-detail")

    def test_card_create_url(self):
        resolver = resolve('/card/create/')
        self.assertEqual(resolver.view_name, "card-create")

    def test_card_create_random_url(self):
        resolver = resolve('/card/random/5/')
        self.assertEqual(resolver.view_name, "card-create-random")

    def test_card_update_url(self):
        resolver = resolve('/card/update/5/')
        self.assertEqual(resolver.view_name, "card-update")

    def test_card_delete_url(self):
        resolver = resolve('/card/delete/5/')
        self.assertEqual(resolver.view_name, "card-delete")
