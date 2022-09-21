from django.test import TestCase
from django.urls import resolve


class TransactionRoutesTestCase(TestCase):
    def test_transaction_list_url(self):
        resolver = resolve('/transaction/list/')
        self.assertEqual(resolver.view_name, "transaction-list")

    def test_transaction_detail_url(self):
        resolver = resolve('/transaction/detail/5/')
        self.assertEqual(resolver.view_name, "transaction-detail")

    def test_transaction_list_between_sums_url(self):
        resolver = resolve('/transaction/list/100/500/')
        self.assertEqual(resolver.view_name, "transaction-between-sums")

    def test_transaction_create_url(self):
        resolver = resolve('/transaction/create/')
        self.assertEqual(resolver.view_name, "transaction-create")

    def test_transaction_create_random_url(self):
        resolver = resolve('/transaction/random/5/')
        self.assertEqual(resolver.view_name, "transaction-create-random")

    def test_transaction_update_url(self):
        resolver = resolve('/transaction/update/5/')
        self.assertEqual(resolver.view_name, "transaction-update")

    def test_transaction_delete_url(self):
        resolver = resolve('/transaction/delete/5/')
        self.assertEqual(resolver.view_name, "transaction-delete")

    def test_transaction_delete_between_dates_url(self):
        resolver = resolve('/transaction/delete/2011-06-05/2015-04-02/')
        self.assertEqual(resolver.view_name,
                         "transaction-delete-between-dates")
