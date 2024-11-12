from pprint import pprint
import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):

    def tearDown(self):
        for key, value in self.all_results.items():
            print(f"{key}: {value}")
        #pprint(self.all_results)
        #pass

    @classmethod
    def setUpClass (cls):
        cls.all_results = {}


    def setUp(self):
        self.runer = runner_and_tournament.Runner("Усэйн")
        self.runer.speed = 10
        self.runer1 = runner_and_tournament.Runner("Андрей")
        self.runer1.speed = 9
        self.runer2 = runner_and_tournament.Runner("Ник")
        self.runer2.speed = 3

    def test_Tournament(self):
        zabeg1 = runner_and_tournament.Tournament(90,self.runer,self.runer2)
        self.all_results.update(zabeg1.start())
        f = max(self.all_results)
        nameoflast = self.all_results[f]
        self.assertTrue(nameoflast == self.runer2)


    def test_Tournament1(self):
        zabeg2 = runner_and_tournament.Tournament(90, self.runer1, self.runer2)
        self.all_results.update(zabeg2.start())
        f = max(self.all_results)
        nameoflast = self.all_results[f]
        self.assertTrue(nameoflast == self.runer2)




    def test_Tournament2(self):
        zabeg3 = runner_and_tournament.Tournament(90, self.runer,self.runer1, self.runer2)
        self.all_results.update(zabeg3.start())
        f = max(self.all_results)
        nameoflast = self.all_results[f]
        self.assertTrue(nameoflast==self.runer2)
