import unittest


def per(a, prev=[]):
    if not a:
        print(prev)
    for index, element in enumerate(a):
        per(a[:index] + a[index + 1:], prev + [element])


def permutations(string):
    if len(string) < 2:
        return [string]
    ar = [c for c in string]
    # print(ar)
    per(ar, [])
    return []


class TestPermutations(unittest.TestCase):
    def test_perm(self):
        self.assertEqual(sorted(permutations('a')), ['a']);
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])
        # self.assertEqual(sorted(permutations('abc')), ['abc', 'acb', 'cab', 'cba', 'bca', 'bac'])
        # self.assertEqual(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
