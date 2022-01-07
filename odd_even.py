import unittest
from typing import List


def odd_or_even(arr: List[int]):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


class TestEven(unittest.TestCase):
    def test_even(self):
        self.assertEqual('even', odd_or_even([2, 2]))
        self.assertEqual('odd', odd_or_even([2, 2, 1]))
