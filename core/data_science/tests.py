from django.test import TestCase
from data_science.models import PlayerBio, Match, Season
from .db_generator import createGenericPlayer

# Create your tests here.


class TotalStats(TestCase):
    def setUp(self):
        pass
    def test_player_generator(self):
        should_be_zero = PlayerBio.objects.all()
        createGenericPlayer('Janusz', 'Korba', 'LW', 'POL', 'Legia Warszawa', 'both') 
        should_be_one = PlayerBio.objects.all()
        self.assertEqual(should_be_one.count(), 1)
        self.assertNotEqual(should_be_zero, should_be_one)
    def test_season_generator(self):
        should_be_zero = Season.objects.all()
        player = createGenericPlayer('Janusz', 'Korba', 'LW', 'POL', 'Legia Warszawa', 'both') 
        should_be_one = Season.objects.all()
        
        self.assertEqual(should_be_one.count(), 1)
        self.assertNotEqual(should_be_zero, should_be_one)
    def test_matches_generator(self):
        should_be_zero = Match.objects.all()
        player = createGenericPlayer('Janusz', 'Korba', 'LW', 'POL', 'Legia Warszawa', 'both') 
        should_be_seventeen = Match.objects.all()
        
        self.assertEqual(should_be_seventeen.count(), 17)
        self.assertNotEqual(should_be_zero, should_be_seventeen)
        