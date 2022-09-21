from django.test import TestCase
from ServiceAPI.models.car import Car
from ServiceAPI.service.car_service import CarService

from ServiceAPI.models.card import Card
from ServiceAPI.service.card_service import CardService

from ServiceAPI.models.transaction import Transaction
from ServiceAPI.service.transaction_service import TransactionService

from datetime import datetime


class DeleteBetweenDatesTestCase(TestCase):
    def setUp(self):
        CarService.createRandom(3, undoredo=False)
        CardService.createRandom(3, undoredo=False)

        Transaction.objects.create(
            car=Car.objects.get(pk=1),
            card=Card.objects.get(pk=1),
            components_price=100,
            workmanship=100,
            datetime=datetime(year=2001, month=1, day=1)
        )

        Transaction.objects.create(
            car=Car.objects.get(pk=2),
            card=Card.objects.get(pk=2),
            components_price=200,
            workmanship=200,
            datetime=datetime(year=2002, month=1, day=1)
        )

        Transaction.objects.create(
            car=Car.objects.get(pk=3),
            card=Card.objects.get(pk=3),
            components_price=300,
            workmanship=300,
            datetime=datetime(year=2004, month=1, day=1)
        )

    def test_delete_between_dates(self):
        self.assertEqual(len(Transaction.objects.all()), 3)
        TransactionService.deleteBetweenDates(
            datetime(year=2000, month=1, day=1),
            datetime(year=2003, month=1, day=1),
            undoredo=False
        )
        self.assertEqual(len(Transaction.objects.all()), 1)
