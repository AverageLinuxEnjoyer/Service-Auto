from django.test import TestCase
from ServiceAPI.models.card import Card
from ServiceAPI.service.card_service import CardService
from datetime import datetime


class UpdateTestCase(TestCase):
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

    def test_update(self):
        lucian = CardService.update(
            Card.objects.create(
                first_name="Lucian",
                last_name="Galan",
                cnp="0123456789123",
                birthday=datetime(year=2002, month=3, day=26),
                registration_date=datetime(year=2012, month=4, day=21)
            ),
            1,
            undoredo=False
        )

        self.assertEqual(lucian, Card.objects.get(pk=1))
