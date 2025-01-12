import unittest
from tour import Runner, Tournament

class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.first = Runner("Усейн", 10)
        self.second = Runner("Андрей", 9)
        self.third = Runner("Ник", 3)

    def tearDown(self):
        for result, keys in self.all_results.items():
            print(f'{result}:{keys}', end=" ")
        print()

    def test_1(self):
        tournament = Tournament(90, self.first, self.third)
        TournamentTest.all_results = tournament.start()
        self.assertTrue(TournamentTest.all_results[max(TournamentTest.all_results.keys())].name == "Ник")

    def test_2(self):
        tournament = Tournament(90, self.second, self.third)
        TournamentTest.all_results = tournament.start()
        self.assertTrue(TournamentTest.all_results[max(TournamentTest.all_results.keys())].name == "Ник")

    def test_3(self):
        tournament = Tournament(90, self.first, self.second, self.third)
        TournamentTest.all_results = tournament.start()
        self.assertTrue(TournamentTest.all_results[max(TournamentTest.all_results.keys())].name == "Ник")