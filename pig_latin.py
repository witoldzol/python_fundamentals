import unittest


def pig_it(word):
    return ' '.join([w[1:] + w[:1] + 'ay' if w.isalpha() else w for w in word.split()])


class TestPigLatin(unittest.TestCase):
    def test_pig(self):
        self.assertEqual(pig_it('Pig latin is cool'), 'igPay atinlay siay oolcay')
        self.assertEqual(pig_it('This is my string'), 'hisTay siay ymay tringsay')
