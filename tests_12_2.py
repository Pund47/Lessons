from pprint import pprint
import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def tearDown(self):
        pprint(self.all_results)
        pass

    @classmethod
    def setUpClass (cls):
        cls.all_results = {}


    def setUp(self):
        runer = runner_and_tournament.Runner("Усэйн")
        runer.speed = 10
        runer1 = runner_and_tournament.Runner("Андрей")
        runer1.speed = 9
        runer2 = runner_and_tournament.Runner("Ник")
        runer2.speed = 3

    def test_Tournament(self, runer,runer1,runer2):
        zabeg1 = runner_and_tournament.Tournament(90,[runer,runer2])
        self.all_results =  zabeg1.start()
        zabeg2 = runner_and_tournament.Tournament(90, [runer1, runer2])
        self.all_results = zabeg2.start()
        zabeg3 = runner_and_tournament.Tournament(90, [runer,runer1, runer2])
        self.all_results = zabeg3.start()
