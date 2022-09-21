from django.test import TestCase
from ServiceAPI.models.card import Card
from ServiceAPI.service.card_service import CardService
from datetime import datetime


class SearchTestCase(TestCase):
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

    def test_search_valid(self):
        cards = CardService.search("12")

        self.assertQuerysetEqual(cards, Card.objects.all(), ordered=False)

    def test_search_no_results(self):
        cards = CardService.search("laborator ubb")

        self.assertNotEqual(cards, Card.objects.all())
        self.assertNotEqual(len(cards), len(Card.objects.all()))
