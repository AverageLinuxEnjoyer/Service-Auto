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

        CarService.create(Car(
            model="Dacia Logan",
            acquisition_date=datetime(year=2011, month=4, day=26),
            kilometers=154900,
            warranty=False
        ))

        self.assertEqual(len(Car.objects.all()), 1)
        UndoRedoService.undo()
        self.assertEqual(len(Car.objects.all()), 0)
        UndoRedoService.redo()
        self.assertEqual(len(Car.objects.all()), 1)

        CardService.create(Card(
            first_name="Lucian",
            last_name="Galan",
            cnp="0123456789123",
            birthday=datetime(year=2002, month=3, day=26),
            registration_date=datetime(year=2012, month=4, day=21)
        ))

        self.assertEqual(len(Card.objects.all()), 1)
        UndoRedoService.undo()
        self.assertEqual(len(Card.objects.all()), 0)
        UndoRedoService.redo()
        self.assertEqual(len(Card.objects.all()), 1)

        UndoRedoService.undo()
        self.assertEqual(len(Card.objects.all()), 0)
        self.assertEqual(len(Car.objects.all()), 1)
        UndoRedoService.undo()
        self.assertEqual(len(Car.objects.all()), 0)

        UndoRedoService.redo()
        UndoRedoService.redo()
        self.assertEqual(len(Card.objects.all()), 1)
        self.assertEqual(len(Car.objects.all()), 1)

        TransactionService.create(Transaction(
            car=Car.objects.get(pk=1),
            card=Card.objects.get(pk=1),
            components_price=100,
            workmanship=100,
            datetime=datetime(year=2022, month=1, day=1)
        ))

        self.assertEqual(len(Car.objects.all()), 1)
        self.assertEqual(len(Card.objects.all()), 1)
        self.assertEqual(len(Transaction.objects.all()), 1)

        UndoRedoService.undo()
        UndoRedoService.undo()
        UndoRedoService.undo()

        self.assertEqual(len(Car.objects.all()), 0)
        self.assertEqual(len(Card.objects.all()), 0)
        self.assertEqual(len(Transaction.objects.all()), 0)
