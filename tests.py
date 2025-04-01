import unittest
from weightlifting_competition.competition import Competition
from weightlifting_competition.competitor import Competitor

karlos = Competitor("Karlos Nasar", "M", "2004-05-12", 89, 180, 225)
karlos.snatch(1, 180, True)
karlos.cnj(1, 225, True)
lasha = Competitor("Lasha Talkhadze", "M", "1993-10-03", 193.3, 180, 225)
lasha.snatch(1, 225, True)
lasha.cnj(1, 267, True)
competition = Competition([karlos, lasha])

class Tester(unittest.TestCase):

    def test_total(self):
        self.assertEqual(karlos.get_total(), 405)
    
    def test_sinclair(self):
        self.assertEqual(karlos.sinclair(), 489.55)
        self.assertEqual(lasha.sinclair(), 492)

    def test_next_lifter(self):
        self.assertLess(karlos.next_snatch, lasha.next_snatch)
        self.assertEqual(competition.next_lifter(), karlos)

    def test_winner(self):
        self.assertEqual(competition.winner(), lasha)

if __name__ == '__main__':
    unittest.main()