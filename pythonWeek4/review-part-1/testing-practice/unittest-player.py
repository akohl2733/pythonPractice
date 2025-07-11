import unittest
from player import Player

class TestPlayerFunction(unittest.TestCase):

    def setUp(self):
        self.instance = Player("Justin Jefferson", "Wide Receiver", "Vikings")

    def test_str(self):
        self.instance.add_touchdowns(10)
        self.instance.add_yards(1400)
        result = str(self.instance)
        self.assertEqual(result, "Justin Jefferson is a Wide Receiver on the Vikings.\nHe has 1400 yards and 10 TDs.")

    def test_touchdown_err(self):
        with self.assertRaises(ValueError):
            self.instance.add_touchdowns('string')

    def test_yards_err(self):
        with self.assertRaises(ValueError):
            self.instance.add_yards("people")

    def test_negative_tds(self):
        with self.assertRaises(ValueError):
            self.instance.add_touchdowns(-90)

    def test_negative_yards(self):
        with self.assertRaises(ValueError):
            self.instance.add_yards(-90)

if __name__ == "__main__":
    unittest.main()
