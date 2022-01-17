import unittest


def _get_score(dice, times):
    if times == 1:
        if dice == 1:
            return 100
        elif dice == 5:
            return 50
        else:
            return 0
    elif times == 2:
        return 0
    else:
        if dice == 1:
            return 1000
        else:
            return dice * 100


def score(scores):
    total = 0
    dic = _count_scores(scores)

    for dice in dic.keys():
        while dic[dice] > 0:
            total += _get_score(dice, dic[dice])
            if dic[dice] > 2:
                dic[dice] -= 3
            else:
                dic[dice] = 0
    return total

def _count_scores(scores):
    dic = {}
    for s in scores:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    return dic


class TestGreed(unittest.TestCase):
    def test_greed(self):
        self.assertEquals(score([2, 3, 4, 6, 2]), 0)
        self.assertEquals(score([4, 4, 4, 3, 3]), 400)
        self.assertEquals(score([2, 4, 4, 5, 4]), 450)
