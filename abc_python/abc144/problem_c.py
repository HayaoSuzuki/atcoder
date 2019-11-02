def make_divisors(n):
    """約数を計算する"""
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


N = int(input())

divisors = make_divisors(N)
ans = min([(a, b) for a, b in zip(divisors, reversed(divisors))], key=lambda x: x[0] + x[1] - 2)
print(ans[0] + ans[1] - 2)
