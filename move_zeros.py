import unittest


def move_zeros(arr):
    arr_without_zeros = [i for i in arr if i != 0]
    number_of_zeros = len(arr) - len(arr_without_zeros)
    return arr_without_zeros + [0] * number_of_zeros


class TestMoveZeros(unittest.TestCase):
    def test_move(self):
        self.assertEqual(move_zeros(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
        self.assertEqual(move_zeros(
            [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 0]), [0, 0])
        self.assertEqual(move_zeros([0]), [0])
        self.assertEqual(move_zeros([]), [])
