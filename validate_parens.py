import unittest


def valid_parentheses(input: str):
    left = 0
    right = 0
    for c in input:
        if c == '(':
            if right > 0:
                right -= 1
            else:
                left += 1
        elif c == ')':
            if left == 0:
                return False
            if left > 0:
                left -= 1
    return left == 0 and right == 0


def better_valid_parentheses(input: str) -> bool:
    count = 0
    for char in input:
        if char == '(': count += 1
        if char == ')': count -= 1
        if count < 0: return False
    return count == 0


class TestParens(unittest.TestCase):
    def test_parens(self):
        self.assertEqual(valid_parentheses("  ("), False, "should work for '  ('")
        self.assertEqual(valid_parentheses(")test"), False, "should work for ')test'")
        self.assertEqual(valid_parentheses(""), True, "should work for ''")
        self.assertEqual(valid_parentheses("hi())("), False, "should work for 'hi())('")
        self.assertEqual(valid_parentheses("hi(hi)()"), True, "should work for 'hi(hi)()'")
        self.assertEqual(better_valid_parentheses("  ("), False, "should work for '  ('")
        self.assertEqual(better_valid_parentheses(")test"), False, "should work for ')test'")
        self.assertEqual(better_valid_parentheses(""), True, "should work for ''")
        self.assertEqual(better_valid_parentheses("hi())("), False, "should work for 'hi())('")
        self.assertEqual(better_valid_parentheses("hi(hi)()"), True, "should work for 'hi(hi)()'")
