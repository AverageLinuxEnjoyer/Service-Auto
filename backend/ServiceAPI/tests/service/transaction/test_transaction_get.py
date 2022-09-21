from django.test import TestCase
from ServiceAPI.models.car import Car
from ServiceAPI.service.car_service import CarService

from ServiceAPI.models.card import Card
from ServiceAPI.service.card_service import CardService

from ServiceAPI.models.transaction import Transaction
from ServiceAPI.service.transaction_service import TransactionService

from datetime import datetime


class GetTestCase(TestCase):
    def setUp(self):
        CarService.createRandom(2, undoredo=False)
        CardService.createRandom(2, undoredo=False)

        Transaction.objects.create(
            car=Car.objects.get(pk=1),
            card=Card.objects.get(pk=1),
            components_price=100,
            workmanship=100,
            datetime=datetime(year=2022, month=1, day=1)
        )

    def test_get_valid(self):
        transaction = TransactionService.get(1)

        self.assertEqual(transaction, Transaction.objects.get(pk=1))

    def test_get_invalid(self):
        returned_from_service = True
        returned_from_django = True

        try:
            transaction_from_service = TransactionService.get(24)
        except Transaction.DoesNotExist as e:
            returned_from_service = False

        try:
            transaction_from_django = Transaction.objects.get(pk=24)
        except Transaction.DoesNotExist as e:
            returned_from_django = False

        self.assertEqual(returned_from_service, returned_from_django)
