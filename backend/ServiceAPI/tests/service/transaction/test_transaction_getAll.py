from django.test import TestCase
from ServiceAPI.models.car import Car
from ServiceAPI.service.car_service import CarService

from ServiceAPI.models.card import Card
from ServiceAPI.service.card_service import CardService

from ServiceAPI.models.transaction import Transaction
from ServiceAPI.service.transaction_service import TransactionService

from datetime import datetime


class GetAllTestCase(TestCase):
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

        Transaction.objects.create(
            car=Car.objects.get(pk=2),
            card=Card.objects.get(pk=2),
            components_price=200,
            workmanship=200,
            datetime=datetime(year=2012, month=2, day=2)
        )

    def test_get_all(self):
        transactions = TransactionService.getAll()

        self.assertQuerysetEqual(
            transactions, Transaction.objects.all(), ordered=False)
