from itertools import product

ans = [a * b for a, b in product(range(1, 10), repeat=2)]

N = int(input())

if N in ans:
    print("Yes")
else:
    print("No")
