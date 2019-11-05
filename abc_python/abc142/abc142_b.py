N, K = tuple(map(int, input().split(" ")))
hs = tuple(map(int, input().split(" ")))

enables = [h for h in hs if h >= K]
print(len(enables))
