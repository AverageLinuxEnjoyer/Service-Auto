from django.test import TestCase
from ServiceAPI.models.car import Car
from ServiceAPI.service.car_service import CarService

from ServiceAPI.models.card import Card
from ServiceAPI.service.card_service import CardService

from ServiceAPI.models.transaction import Transaction
from ServiceAPI.service.transaction_service import TransactionService

from datetime import datetime


class CreateRandomTestCase(TestCase):
    def setUp(self):
        CarService.createRandom(2, undoredo=False)
        CardService.createRandom(2, undoredo=False)

    def test_create_random(self):
        created_transactions = TransactionService.createRandom(
            5, undoredo=False)

        total_transactions = len(created_transactions)

        self.assertEqual(total_transactions, 5)
        self.assertEqual(total_transactions, len(Transaction.objects.all()))
