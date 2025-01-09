import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = Runner("walker")
        for _ in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        runner = Runner("runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        first = Runner("first")
        second = Runner("second")
        for _ in range(10):
            first.run()
            second.walk()
        self.assertNotEquals(first.distance, second.distance)
