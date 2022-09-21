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
    def test_create(self):
        self.assertEqual(len(Car.objects.all()), 0)
        self.assertEqual(len(Card.objects.all()), 0)
        self.assertEqual(len(Transaction.objects.all()), 0)

        CarService.createRandom(2)

        self.assertEqual(len(Car.objects.all()), 2)
        UndoRedoService.undo()
        self.assertEqual(len(Car.objects.all()), 0)
        UndoRedoService.redo()
        self.assertEqual(len(Car.objects.all()), 2)

        CardService.createRandom(5)

        self.assertEqual(len(Card.objects.all()), 5)
        UndoRedoService.undo()
        self.assertEqual(len(Card.objects.all()), 0)
        UndoRedoService.redo()
        self.assertEqual(len(Card.objects.all()), 5)

        UndoRedoService.undo()
        self.assertEqual(len(Card.objects.all()), 0)
        self.assertEqual(len(Car.objects.all()), 2)
        UndoRedoService.undo()
        self.assertEqual(len(Car.objects.all()), 0)

        UndoRedoService.redo()
        UndoRedoService.redo()
        self.assertEqual(len(Card.objects.all()), 5)
        self.assertEqual(len(Car.objects.all()), 2)

        TransactionService.createRandom(10)

        self.assertEqual(len(Car.objects.all()), 2)
        self.assertEqual(len(Card.objects.all()), 5)
        self.assertEqual(len(Transaction.objects.all()), 10)

        UndoRedoService.undo()
        UndoRedoService.undo()
        UndoRedoService.undo()

        self.assertEqual(len(Car.objects.all()), 0)
        self.assertEqual(len(Card.objects.all()), 0)
        self.assertEqual(len(Transaction.objects.all()), 0)
