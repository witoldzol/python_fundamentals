import unittest


def to_arr(str):
    return [c for c in str]


def rot(c):
    if 'a' <= c <= 'z':
        return move_13(ord('a'), ord('z'), ord(c))
    elif 'A' <= c <= 'Z':
        return move_13(ord('A'), ord('Z'), ord(c))
    return c


def move_13(start, end, code):
    moved = code + 13
    if moved > end:
        moved = moved - end + start - 1
    return chr(moved)


def rot13(str):
    arr = to_arr(str)
    moved_arr = [rot(c) for c in arr]
    return ''.join(moved_arr)


class TestRot13(unittest.TestCase):
    def test_rot(self):
        self.assertEquals(rot13("test"), "grfg")
        self.assertEquals(rot13("Test"), "Grfg")
