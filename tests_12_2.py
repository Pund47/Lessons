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
        self.runer = runner_and_tournament.Runner("Усэйн")
        self.runer.speed = 10
        self.runer1 = runner_and_tournament.Runner("Андрей")
        self.runer1.speed = 9
        self.runer2 = runner_and_tournament.Runner("Ник")
        self.runer2.speed = 3

    def test_Tournament(self):
        zabeg1 = runner_and_tournament.Tournament(90,self.runer,self.runer2)
        self.all_results =  zabeg1.start()
        #zabeg2 = runner_and_tournament.Tournament(90, self.runer1, self.runer2)
        #self.all_results = zabeg2.start()
        #zabeg3 = runner_and_tournament.Tournament(90, self.runer,self.runer1, self.runer2)
        #self.all_results = zabeg3.start()

        self.assertTrue(max(self.all_results, key=self.all_results.get(len(self.all_results)))=="Ник")
