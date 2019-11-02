N = int(input())
S = input()

current = ""
result = []

for slime in S:
    if slime == current:
        continue
    else:
        current = slime
        result.append(slime)
print(len(result))
