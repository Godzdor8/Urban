import unittest
from tour import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        walker = Runner("walker")
        for _ in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner("runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        first = Runner("first")
        second = Runner("second")
        for _ in range(10):
            first.run()
            second.walk()
        self.assertNotEquals(first.distance, second.distance)

class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.first = Runner("Усейн", 10)
        self.second = Runner("Андрей", 9)
        self.third = Runner("Ник", 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def tearDown(self):
        for result, keys in self.all_results.items():
            print(f'{result}:{keys}', end=" ")
        print()

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_1(self):
        tournament = Tournament(90, self.first, self.third)
        TournamentTest.all_results = tournament.start()
        self.assertTrue(TournamentTest.all_results[max(TournamentTest.all_results.keys())].name == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_2(self):
        tournament = Tournament(90, self.second, self.third)
        TournamentTest.all_results = tournament.start()
        self.assertTrue(TournamentTest.all_results[max(TournamentTest.all_results.keys())].name == "Ник")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_3(self):
        tournament = Tournament(90, self.first, self.second, self.third)
        TournamentTest.all_results = tournament.start()
        self.assertTrue(TournamentTest.all_results[max(TournamentTest.all_results.keys())].name == "Ник")