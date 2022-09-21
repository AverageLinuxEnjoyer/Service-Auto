from django.test import TestCase
from ServiceAPI.models.card import Card
from ServiceAPI.service.card_service import CardService
from datetime import datetime


class GetTestCase(TestCase):
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

    def test_get_valid(self):
        lucian = CardService.get(1)

        self.assertEqual(lucian, Card.objects.get(pk=1))

    def test_get_invalid(self):
        returned_from_service = True
        returned_from_django = True

        try:
            card_from_service = CardService.get(24)
        except Card.DoesNotExist as e:
            returned_from_service = False

        try:
            card_from_django = Card.objects.get(pk=24)
        except Card.DoesNotExist as e:
            returned_from_django = False

        self.assertEqual(returned_from_service, returned_from_django)
