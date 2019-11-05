from math import ceil
from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


S = input()
K = int(input())

if len(S) == 1:
    print(K // 2)
else:
    print(ceil(sum(1 for s, t in pairwise(S) if s == t) / 2) * K)
