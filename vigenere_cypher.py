import unittest


class VigenereCipher:

    def __init__(self, key: str, abc: str):
        self.abc = abc
        self.key = self._match_abc(key, abc)

    def encode(self, text: str) -> str:
        encoded = ''
        for i, char in enumerate(text):
            shift_by_key = self.abc.index(self.key[i])
            starting_index = self.abc.index(char) if char in self.abc else -1
            total_index = starting_index + shift_by_key
            if total_index >= len(self.abc):
                total_index = total_index - len(self.abc)
            encoded += self.abc[total_index] if starting_index != -1 else text[i]
        return encoded

    def decode(self, text:str):
        encoded = ''
        for i, char in enumerate(text):
            shift_by_key = self.abc.index(self.key[i])
            starting_index = self.abc.index(char) if char in self.abc else -1
            if starting_index == -1:
                encoded += text[i]
            elif starting_index != -1 and shift_by_key > starting_index:
                total_index = shift_by_key - starting_index
                encoded += self.abc[-total_index]
            else:
                total_index = starting_index - shift_by_key
                encoded += self.abc[total_index]

        return encoded


    def _match_abc(self, key, abc):
        if len(key) >= len(abc):
            return key[:len(abc)]
        times = int(len(abc) / len(key)) + 1
        return (key * times)[:len(abc)]


class TestVigenereCypher(unittest.TestCase):
    def test_cypher(self):
        abc = "abcdefghijklmnopqrstuvwxyz"
        key = "password"
        c = VigenereCipher(key, abc)

        self.assertEqual('r', c.encode('c'))
        self.assertEqual('c', c.decode('r'))

        self.assertEqual(c.encode('codewars'), 'rovwsoiv')
        self.assertEqual(c.decode('rovwsoiv'), 'codewars')

        self.assertEqual(c.encode('waffles'), 'laxxhsj')
        self.assertEqual(c.decode('laxxhsj'), 'waffles')

        self.assertEqual(c.encode('CODEWARS'), 'CODEWARS')
        self.assertEqual(c.decode('CODEWARS'), 'CODEWARS')

    def test_match_abc(self):
        self.assertEqual('abcabc', VigenereCipher(key='abc', abc='abcdef').key)
        self.assertEqual('abca', VigenereCipher(key='abc', abc='abcd').key)
        self.assertEqual('abc', VigenereCipher(key='abcde', abc='xyz').key)
        self.assertEqual('abcabc', VigenereCipher(key='abc', abc='x y z ').key)
