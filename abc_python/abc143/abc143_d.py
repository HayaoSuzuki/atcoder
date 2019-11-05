from itertools import combinations
from array import array

N = int(input())
lengths = array('I', sorted(map(int, input().split(" "))))

for x, y, z in combinations(lengths, 3):
    if z < x + y:
        print(x, y, z)




print(len(list(combinations(lengths, 2))))
print(len(list(combinations(lengths, 3))))
