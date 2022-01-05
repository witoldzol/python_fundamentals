import unittest
from functools import reduce


def sum_array(arr):
    sum = 0
    for x in arr:
        sum += x
    return sum


def isDivisibleBy(x, n):
    return x % n == 0


def solution(number):
    dividers = []
    try:
        for x in range(1, number):
            if isDivisibleBy(x, 3) or isDivisibleBy(x, 5):
                dividers.append(x)
        # return reduce(lambda a, b: a + b, dividers)
        return sum_array(dividers)
    except Exception:
        return 0


def alternative(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


class TestSumDividers(unittest.TestCase):
    def test_sample(self):
        self.assertEquals(solution(4), 3)
        self.assertEquals(solution(6), 8)
        self.assertEquals(solution(16), 60)
        self.assertEquals(solution(3), 0)
        self.assertEquals(solution(5), 3)
        self.assertEquals(solution(15), 45)
        self.assertEquals(solution(0), 0)
        self.assertEquals(solution(-1), 0)
        self.assertEquals(solution(10), 23)
        self.assertEquals(solution(20), 78)
        self.assertEquals(solution(200), 9168)

    def test_alternative(self):
        self.assertEquals(alternative(4), 3)
        self.assertEquals(alternative(6), 8)
        self.assertEquals(alternative(16), 60)
        self.assertEquals(alternative(3), 0)
        self.assertEquals(alternative(5), 3)
        self.assertEquals(alternative(15), 45)
        self.assertEquals(alternative(0), 0)
        self.assertEquals(alternative(-1), 0)
        self.assertEquals(alternative(10), 23)
        self.assertEquals(alternative(20), 78)
        self.assertEquals(alternative(200), 9168)
