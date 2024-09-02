from itertools import permutations
import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))


def absSub(a, b):
    return abs(a - b)

rst = list(permutations(lst, n))

max = 0

for i in rst:
    sum = 0
    for j in range(n - 1):
        sum += absSub(i[j], i[j + 1])

    if sum > max:
        max = sum

print(max)