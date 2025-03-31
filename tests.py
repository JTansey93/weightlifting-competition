import unittest
from weightlifting_competition.competition import Competition
from weightlifting_competition.competitor import Competitor

class TestCompetitor(unittest.TestCase):

    def test_total(self):
        karlos = Competitor("Karlos Nasar", "M", "2004-05-12", 89)
        karlos.snatch(1, 170, True)
        karlos.cnj(1, 210, True)
        self.assertEqual(karlos.get_total(), 380)
        self.assertEqual(karlos.sinclair(), 459.33)

if __name__ == '__main__':
    unittest.main()