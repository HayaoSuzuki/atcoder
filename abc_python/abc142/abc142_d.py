from math import gcd


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


A, B = tuple(map(int, input().split(" ")))

print(len(set(prime_factorize(gcd(A, B)))) + 1)
