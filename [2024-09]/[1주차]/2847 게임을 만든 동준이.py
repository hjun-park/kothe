import sys

n = int(sys.stdin.readline())

lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))

rst = [0] * (n + 1)

for i in range(n - 1, 0, -1):
    while lst[i] <= lst[i - 1]:
        rst[i] += 1
        lst[i - 1] -= 1

print(sum(rst))

