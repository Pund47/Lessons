import unittest
from unittest import TestSuite, TestLoader
import tests_12_4_1 as my_test
import logging


RunnerTest     = unittest.TestSuite()
RunnerTest.addTest(unittest.TestLoader().loadTestsFromTestCase(my_test.TournamentTest))




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,filemode="w",filename="runner_tests.log",encoding="UTF-8",
                        format="%(asctime)s | %(levelname)s | %(message)s")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(RunnerTest)

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())