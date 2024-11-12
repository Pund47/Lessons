import runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen == True,"ok")
    def test_walk(self):
        gulyaka = runner.Runner("gulyaka")
        for i in range (10):
            gulyaka.walk()
        self.assertEqual(gulyaka.distance,50)

    @unittest.skipIf(is_frozen == True, "ok")
    def test_run(self):
        runer = runner.Runner("runer")
        for i in range (10):
            runer.run()
        self.assertEqual(runer.distance, 100)

    @unittest.skipIf(is_frozen == True, "ok")
    def test_challenge (self):
        gulyaka = runner.Runner("gulyaka")
        runer = runner.Runner("runer")
        for i in range (10):
            runer.run()
            gulyaka.walk()
        self.assertNotEqual(gulyaka.distance,runer.distance)


if __name__ == '__main__':
    unittest.main()


