from itertools import combinations

N = int(input())
takoyaki = map(int, input().split(" "))

score = 0
for x, y in combinations(takoyaki, 2):
    score += x * y
print(score)
