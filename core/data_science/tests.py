from django.test import TestCase
from data_science.models import PlayerBio, Match, Season

# Create your tests here.


class TotalStats(TestCase):
    def setUp(self):
        self.player = PlayerBio.objects.create()