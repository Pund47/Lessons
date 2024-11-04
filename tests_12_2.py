import runner_and_tournament
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def tearDown(cls):
        print(all_results)

    def setUpClass (self):
        all_results = []
        all_results[self.name]= self.distance

    def setUp(self):
        runer = runner_and_tournament.Runner("Усэйн")
        runer.speed = 10
        runer1 = runner_and_tournament.Runner("Андрей")
        runer1.speed = 9
        runer2 = runner_and_tournament.Runner("Ник")
        runer2.speed = 3
    def test_Tournament(self):
        zabeg1 = runner_and_tournament.Tournament(90,[runer,runer2])
        zabeg2 = runner_and_tournament.Tournament(90, [runer1, runer2])
        zabeg3 = runner_and_tournament.Tournament(90, [runer,runer1, runer2])

        pass