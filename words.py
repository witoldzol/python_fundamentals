from urllib.request import urlopen


def get_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for lin in line_words:
            words.append(lin)

    story.close()
    for x in words:
        print(x)


def get_square_root(radicand, nth):
    return radicand ** (1 / nth)

