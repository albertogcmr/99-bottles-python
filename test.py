from nn_bottles import nn_bottles
from collections import Counter


def test_lyric_generator():
    res = False
    s1 = None

    # Open textfile
    with open('99-bottles-original.txt', 'r') as f:
        s1 = f.read()

    # print(s1)
    s2 = nn_bottles(99)
    # print(s2)
    # print(s1 == s2)
    print('Archivo y string son idénticos:', s1 == s2)

    c1 = Counter(s1)
    c2 = Counter(s2)
    print(c1)
    print(c2)
    print('Ambos diccionarios son idénticos:', c1 == c2)
    return s1 == s2


def test_char_vs_char():
    res = True
    s1 = None

    # Open textfile
    with open('99-bottles-original.txt', 'r') as f:
        s1 = f.read()

    s2 = nn_bottles(99)
    # print(s1 == s2)
    for x, y in zip(s1, s2):
        # print(x, y)
        if x is not y:
            print('{} is not {}'.format(x, y))
            res = False
            break
    if res is True:
        print('Ambas cadenas son idénticas carácter a carácter')
    return res


if __name__ == '__main__':
    test_lyric_generator()
    test_char_vs_char()
