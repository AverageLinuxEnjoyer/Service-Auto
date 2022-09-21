from django.test import TestCase
from ServiceAPI.models.car import Car
from ServiceAPI.service.car_service import CarService

from ServiceAPI.models.card import Card
from ServiceAPI.service.card_service import CardService

from ServiceAPI.models.transaction import Transaction
from ServiceAPI.service.transaction_service import TransactionService

from ServiceAPI.service.undo_redo_service import UndoRedoService

from datetime import datetime


class CreateTestCase(TestCase):
    def setUp(self):
        CarService.createRandom(5)
        CardService.createRandom(5)
        TransactionService.createRandom(5)

    def test_delete(self):
        self.assertEqual(len(Car.objects.all()), 5)
        self.assertEqual(len(Card.objects.all()), 5)
        self.assertEqual(len(Transaction.objects.all()), 5)

        CarService.delete(id=3)
        self.assertEqual(len(Car.objects.all()), 4)
        UndoRedoService.undo()
        self.assertEqual(len(Car.objects.all()), 5)
        UndoRedoService.redo()
        self.assertEqual(len(Car.objects.all()), 4)

        CardService.delete(id=3)
        self.assertEqual(len(Card.objects.all()), 4)
        UndoRedoService.undo()
        self.assertEqual(len(Card.objects.all()), 5)
        UndoRedoService.redo()
        self.assertEqual(len(Card.objects.all()), 4)

        TransactionService.delete(id=1)
        self.assertEqual(len(Transaction.objects.all()), 4)
        UndoRedoService.undo()
        self.assertEqual(len(Transactionar.objects.all()), 5)
        UndoRedoService.redo()
        self.assertEqual(len(Transaction.objects.all()), 4)
