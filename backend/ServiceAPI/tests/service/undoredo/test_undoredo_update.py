from django.test import TestCase
from ServiceAPI.models.car import Car
from ServiceAPI.service.car_service import CarService

from ServiceAPI.models.card import Card
from ServiceAPI.service.card_service import CardService

from ServiceAPI.models.transaction import Transaction
from ServiceAPI.service.transaction_service import TransactionService

from ServiceAPI.service.undo_redo_service import UndoRedoService

from datetime import datetime, date


class UpdateTestCase(TestCase):
    def setUp(self):
        CarService.create(Car(
            model="Dacia Logan",
            acquisition_date=datetime(year=2011, month=4, day=26),
            kilometers=154900,
            warranty=False
        ), undoredo=False)

        CardService.create(Card(
            first_name="Lucian",
            last_name="Galan",
            cnp="0123456789123",
            birthday=datetime(year=2002, month=3, day=26),
            registration_date=datetime(year=2012, month=4, day=21)
        ), undoredo=False)

        TransactionService.create(Transaction(
            car=Car.objects.get(pk=1),
            card=Card.objects.get(pk=1),
            components_price=100,
            workmanship=100,
            datetime=datetime(year=2022, month=1, day=1)
        ), undoredo=False)

    def test_update(self):
        self.assertEqual(CarService.get(id=1).model, "Dacia Logan")
        self.assertEqual(CardService.get(id=1).first_name, "Lucian")
        self.assertEqual(TransactionService.get(id=1).workmanship, 90)

        CarService.update(new_car=Car(
            model="Dacia Duster",
            acquisition_date=date(year=2011, month=4, day=26),
            kilometers=154900,
            warranty=False
        ), id=1)

        self.assertEqual(CarService.get(id=1).model, "Dacia Duster")
        UndoRedoService.undo()
        self.assertEqual(CarService.get(id=1).model, "Dacia Logan")
        UndoRedoService.redo()
        self.assertEqual(CarService.get(id=1).model, "Dacia Duster")

        CardService.update(new_card=Card(
            first_name="Lucian Gabriel",
            last_name="Galan",
            cnp="0123456789123",
            birthday=date(year=2002, month=3, day=26),
            registration_date=date(year=2012, month=4, day=21)
        ), id=1)

        self.assertEqual(CardService.get(id=1).first_name, "Lucian Gabriel")
        UndoRedoService.undo()
        self.assertEqual(CardService.get(id=1).first_name, "Lucian")
        UndoRedoService.redo()
        self.assertEqual(CardService.get(id=1).first_name, "Lucian Gabriel")

        TransactionService.update(new_transaction=Transaction(
            car=Car.objects.get(pk=1),
            card=Card.objects.get(pk=1),
            components_price=100,
            workmanship=500,
            datetime=datetime(year=2022, month=1, day=1)
        ), id=1)

        self.assertEqual(TransactionService.get(id=1).workmanship, 500)
        UndoRedoService.undo()
        self.assertEqual(TransactionService.get(id=1).workmanship, 90)
        UndoRedoService.redo()
        self.assertEqual(TransactionService.get(id=1).workmanship, 500)
