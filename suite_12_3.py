import unittest
from unittest import TestSuite, TestLoader
import module_12_1 as my_test1
import Test_12_2   as my_test2


RunnerTest     = unittest.TestSuite()
RunnerTest.addTest(unittest.TestLoader().loadTestsFromTestCase(my_test1.RunnerTest))
RunnerTest.addTest(unittest.TestLoader().loadTestsFromTestCase(my_test2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(RunnerTest)


