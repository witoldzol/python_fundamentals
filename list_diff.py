import unittest


def array_diff(l1, l2):
    return [x for x in l1 if x not in set(l2)]


class TestListDiff(unittest.TestCase):
    def test_bob(self):
        self.assertEquals(array_diff([1, 2], [1]), [2], "a was [1,2], b was [1], expected [2]")
        self.assertEquals(array_diff([1, 2, 2], [1]), [2, 2], "a was [1,2,2], b was [1], expected [2,2]")
        self.assertEquals(array_diff([1, 2, 2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
        self.assertEquals(array_diff([1, 2, 2], []), [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]")
        self.assertEquals(array_diff([], [1, 2]), [], "a was [], b was [1,2], expected []")
        self.assertEquals(array_diff([1, 2, 3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")
