from django.test import TestCase
from ServiceAPI.models.card import Card
from ServiceAPI.service.card_service import CardService
from datetime import datetime


class DeleteTestCase(TestCase):
    def setUp(self):
        Card.objects.create(
            first_name="Lucian",
            last_name="Galan",
            cnp="0123456789123",
            birthday=datetime(year=2002, month=3, day=26),
            registration_date=datetime(year=2012, month=4, day=21)
        )

        Card.objects.create(
            first_name="Mihai",
            last_name="Popescu",
            cnp="0123456789124",
            birthday=datetime(year=1986, month=8, day=5),
            registration_date=datetime(year=2018, month=3, day=22)
        )

    def test_delete_valid(self):
        initial_card_count = len(Card.objects.all())

        CardService.delete(1, undoredo=False)

        new_card_count = len(Card.objects.all())

        self.assertEqual(new_card_count, 1)
        self.assertNotEqual(initial_card_count, new_card_count)

    def test_delete_invalid(self):
        initial_card_count = len(Card.objects.all())

        try:
            CardService.delete(5, undoredo=False)
        except Card.DoesNotExist as e:
            pass

        new_card_count = len(Card.objects.all())

        self.assertEqual(initial_card_count, new_card_count)
