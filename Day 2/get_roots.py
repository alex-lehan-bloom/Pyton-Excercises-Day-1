import math


def get_roots(a, b, c):
    b = b * -1
    x1 = lambda a, b, c: (b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = lambda a, b, c: (b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print("X={}, X={}".format(x1(a, b, c), x2(a, b, c)))


get_roots(1, 3, -4)
