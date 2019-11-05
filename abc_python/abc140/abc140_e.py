from itertools import islice, combinations


def nth(iterable, n, default=None):
    return next(islice(iterable, n, None), default)


N = int(input())
P = tuple(map(int, input().split(" ")))

s = 0
for L, R in combinations(range(1, N + 1), 2):
    # print(list(islice(P, L - 1, R)))
    if R == L + 1:
        s += min(islice(P, L - 1, R))
        continue
    ll = sorted(islice(P, L - 1, R), reverse=True)
    s += nth(ll, 1)
else:
    print(s)
