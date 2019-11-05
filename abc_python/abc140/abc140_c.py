from itertools import tee


def pairwise(iterable):
    x, y = tee(iterable)
    next(y, None)
    return zip(x, y)


n = int(input())
b = tuple(map(int, input().split(" ")))

if len(b) == 1:
    print(2 * b[0])
else:
    s = b[0] + sum(min((i, j)) for i, j in pairwise(b)) + b[-1]
    print(s)
