import unittest

cache = {}


def calc_total_elements(max, n, curr):
    if n in cache:
        return cache.get(n)

    if n < 2:
        return n

    updated = pow(n, 3) + curr
    if updated > max:
        return -1

    return pow(n, 3) + calc_total_elements(max, n - 1, updated)


def find_nb(m):
    n = int(m ** (1 / float(3)))

    for i in range(1, n):
        r = calc_total_elements(m, i, 0)
        cache[i] = r
        if r == m:
            print(f' found the number {r}')
            return i

    return -1


class TestCubic(unittest.TestCase):
    def test_cube(self):
        self.assertEqual(find_nb(4183059834009), 2022)
        self.assertEqual(find_nb(24723578342962), -1)
        self.assertEqual(find_nb(135440716410000), 4824)
        self.assertEqual(find_nb(40539911473216), 3568)
        self.assertEqual(find_nb(26825883955641), 3218)
