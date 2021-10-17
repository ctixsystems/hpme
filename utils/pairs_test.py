import unittest

from utils.pairs import make_round_pairs

class TestPairs(unittest.TestCase):
    def test_sequence(self):
        sequence = ['A', 'B', 'C', 'D']
        expected = [('A','B'), ('B','C'), ('C','D'), ('D','A')]
        actual = make_round_pairs(sequence)

        self.assertEqual(expected, actual)
