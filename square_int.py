import unittest


def square_digits(num):
    return int(''.join([str(int(x) ** 2) for x in str(num)]))


class Test_Square(unittest.TestCase):

    def test_square(self):
        self.assertEqual(1, square_digits(1))
        self.assertEqual(0, square_digits(0))
        self.assertEqual(16, square_digits(4))
        self.assertEqual(1616, square_digits(44))
        self.assertEqual(161160, square_digits(4140))
