import logging
import unittest
from logs import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_tests.log", encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            walker = Runner("walker", -5)
            logging.info('"test_walk" выполнен успешно')
            for _ in range(10):
                walker.walk()
            self.assertEqual(walker.distance, 50)
        except ValueError:

            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            runner = Runner(5)
            logging.info('"test_run" выполнен успешно')
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

