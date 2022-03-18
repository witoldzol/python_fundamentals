import unittest

ROMANS = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'C': 100,
    'XC': 90,
    'L': 50,
    'X': 10,
    'V': 5,
    'IV': 4,
    'I': 1,
}


class RomanNumerals:
    def to_roman(number: int) -> str:
        s = ''
        for k, v in ROMANS.items():
            print(f'key is {k} value {v}')
            while number % v != number:
                number = number - v
                s += k
        return s

    def from_roman(r):
        s = 0
        for key, value in ROMANS.items():
            while r.startswith(key):
                r = r[len(key):]
                s += value
        return s

class MyRomanNumerals:
    @classmethod
    def to_roman(self, number: int) -> str:
        int_to_roman: dict = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        final_roman = ''
        reminder = number
        s = sorted(int_to_roman.keys(), reverse=True)
        for x in s:
            if reminder == 0: break
            times = int(reminder / x)
            reminder = reminder % x
            roman_number = int_to_roman[x]
            final_roman += (roman_number * times)
        return final_roman

    @classmethod
    def from_roman(self, roman_number: str) -> int:
        map: dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        final_int = 0
        skip = False
        next = ''
        for i, curr in enumerate(roman_number):
            if skip:
                skip = False
                continue
            if i + 1 < len(roman_number):
                next = roman_number[i + 1]
                if map[curr] < map[next]:
                    final_int += map[next] - map[curr]
                    skip = True
                    continue
            final_int += map[curr]
        return final_int


class TestRomanNumerals(unittest.TestCase):
    def test_to(self):
        self.assertEqual(RomanNumerals.to_roman(1000), 'M', '1000 should == "M"')
        self.assertEqual(RomanNumerals.to_roman(4), 'IV', '4 should == "IV"')
        self.assertEqual(RomanNumerals.to_roman(1), 'I', '1 should == "I"')
        self.assertEqual(RomanNumerals.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')
        self.assertEqual(RomanNumerals.to_roman(2008), 'MMVIII', '2008 should == "MMVIII"')


    def test_from_roman(self):
        self.assertEqual(RomanNumerals.from_roman('XXI'), 21, 'XXI should == 21')
        self.assertEqual(RomanNumerals.from_roman('I'), 1, 'I should == 1')
        self.assertEqual(RomanNumerals.from_roman('IV'), 4, 'IV should == 4')
        self.assertEqual(RomanNumerals.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')
        self.assertEqual(RomanNumerals.from_roman('MDCLXVI'), 1666, 'MDCLXVI should == 1666')
