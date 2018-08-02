"""
http://www.99-bottles-of-beer.net/
Autor: garcia.cobo.alberto@gmail.com
"""


def nn_bottles(b_max):
    res = ""

    def bottles(n):
        s = "s"
        result = '{0} bottle{1} of beer'
        if n == 1:
            s = ""
        return result.format(n, s)

    for i in range(b_max, 0, -1):
        n1, n0 = bottles(i), bottles(i-1)
        if i == 1:
            n0 = 'no more bottles of beer'
        res += '{0} on the wall, {0}.'.format(n1)
        res += '\nTake one down and pass it around, {0} on the wall.\n\n'.format(n0)

    res += '{0} on the wall, {1}.\nGo to the store and buy some more, {2} on the wall.'.format(n0.capitalize(),
                                                                                               n0,
                                                                                               bottles(99))
    return res

if __name__ == '__main__':
    print(nn_bottles(99))
