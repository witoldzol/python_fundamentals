import unittest


def pick_peaks(arr):
    peaks = {'pos': [], 'peaks': []}
    prob_peak = False
    for p in range(1, len(arr)):  # range is not enclosed at the end !!!!
        if arr[p] > arr[p - 1]:
            prob_peak = p
        elif arr[p] < arr[p - 1] and prob_peak:
            peaks['pos'].append(prob_peak)
            peaks['peaks'].append(arr[prob_peak])
            prob_peak = False

    return peaks


# def pick_peaks(arr):
#     peaks = {'pos': [], 'peaks': []}
#     if len(arr) < 3:
#         return peaks
#
#     for x in range(1, len(arr) - 1):
#         if arr[x] > arr[x - 1]:
#             if arr[x] > arr[x + 1]:
#                 peaks['pos'].append(x)
#                 peaks['peaks'].append(arr[x])
#             elif arr[x] == arr[x + 1]:
#                 for y in range(x + 1, len(arr)):
#                     if arr[x] > arr[y]:
#                         peaks['pos'].append(x)
#                         peaks['peaks'].append(arr[x])
#                         break
#                     elif arr[x] < arr[y]:
#                         break
#     return peaks


class TestFindPeaks(unittest.TestCase):
    def test_peaks(self):
        self.assertEqual(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]), {"pos": [3, 7], "peaks": [6, 3]})
        self.assertEqual(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]), {"pos": [3, 7], "peaks": [6, 3]})
        self.assertEqual(pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1]), {"pos": [3, 7, 10],
                                                                                  "peaks": [6, 3, 2]})
        self.assertEqual(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2, 1]), {"pos": [2, 4], "peaks": [3, 2]})
        self.assertEqual(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]), {"pos": [2], "peaks": [3]})
        self.assertEqual(pick_peaks([2, 1, 3, 2, 2, 2, 2, 5, 6]), {"pos": [2], "peaks": [3]})
        self.assertEqual(pick_peaks([2, 1, 3, 2, 2, 2, 2, 1]), {"pos": [2], "peaks": [3]})
        self.assertEqual(pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]), {
            "pos": [2, 7, 14, 20], "peaks": [5, 6, 5, 5]})
        self.assertEqual(pick_peaks([18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13,
                                     9, 16, 18, 6, 7]), {'pos': [5, 9, 12, 14, 16, 20, 23],
                                                         'peaks': [15, 17, 18, 19, 18, 13, 18]})
        self.assertEqual(pick_peaks([]), {"pos": [], "peaks": []})
        self.assertEqual(pick_peaks([1, 1, 1, 1]), {"pos": [], "peaks": []})
