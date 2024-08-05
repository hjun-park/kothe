import sys

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        lst.append(num)
    else:
        lst.pop()

print(sum(lst))
