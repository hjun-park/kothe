import sys

lst = [0] * 30

for i in range(0, 28):
    index = int(sys.stdin.readline())
    lst[index - 1] = 1

rst = [i + 1 for i, value in enumerate(lst) if value == 0]

for i in rst:
    print(i)
