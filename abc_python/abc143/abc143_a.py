A, B = map(int, input().split(" "))

length = A - 2 * B
if length >= 0:
    print(length)
else:
    print(0)
