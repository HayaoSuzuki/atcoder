N = int(input())
A = list(map(int, input().split(" ")))

d = dict(zip(range(N), A))

ans = [str(k + 1) for k, _ in sorted(d.items(), key=lambda x: x[1])]
print(" ".join(ans))
