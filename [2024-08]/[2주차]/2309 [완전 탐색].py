import sys
from itertools import combinations

lst = []
for i in range(9):
    lst.append(int(sys.stdin.readline()))

rst = []
for i in list(combinations(lst, 7)):
    if (sum(i) == 100):
        rst = list(i)
        break

for i in sorted(rst):
    print(i)
