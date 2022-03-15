import unittest


def max_sequence(arr):
    if len(arr) == 0:
        return 0
    d = {"start": 0, "end": 0, "max": 0}
    for i, x in enumerate(arr):
        curr = 0
        for idx, y in enumerate(arr[i:]):
            curr += y
            if curr >= d["max"]:
                d["start"] = i
                d["end"] = idx
                d["max"] = curr
    return d["max"]


def better_max_sequence(arr):
    if not len(arr): return 0
    max, curr = 0, 0
    for x in arr:
        curr += x
        if curr < 0: curr = 0
        if curr > max: max = curr
    return max


class TestMaxSequence(unittest.TestCase):
    def test_sub(self):
        # self.assertEqual(max_sequence([]), 0)
        # self.assertEqual(6, max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        self.assertEqual(better_max_sequence([]), 0)
        self.assertEqual(6, better_max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
