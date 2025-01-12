import unittest
import tests_12_3


RunnerTS = unittest.TestSuite()
RunnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
RunnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(RunnerTS)



