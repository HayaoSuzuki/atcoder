n = int(input())

odds = len([x for x in range(1, n + 1) if x % 2 == 1])
print(odds / n)
