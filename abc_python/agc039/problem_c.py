from functools import lru_cache

N = int(input())
X = int(input(), 2)


@lru_cache(maxsize=None)
def calc(k: int):
    if k % 2 == 0:
        k = (k // 2)
        k += pow(2, N - 1)
    else:
        k = (k - 1) // 2
    return k


total = 0
for x in range(X + 1):
    k = x
    org_k = x
    c = 0
    # print(x, c, bin(k))
    while True:
        k = calc(k)
        c += 1
        # print(c, bin(k))
        if k == org_k:
            break
    total += c
    # print()

print(total)
