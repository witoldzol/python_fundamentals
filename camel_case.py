import unittest

def to_camel_case(word):
    return word[:1] + word.title()[1:].replace('_', '').replace('-', '')


def to_camel_case2(word):
    if len(word) == 0:
        return ''
    else:
        output = ''
        upCase = False
        for c in word:
            if c == '_' or c == '-':
                upCase = True
                continue
            if upCase:
                output += c.upper()
                upCase = False
            else:
                output += c

        return output


class TestCamelCase(unittest.TestCase):
    def test_camel(self):
        self.assertEqual(to_camel_case(''), '', "An empty string was provided but not returned")
        self.assertEqual(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
        self.assertEqual(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
        self.assertEqual(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")
