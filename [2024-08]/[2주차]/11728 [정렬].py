import sys

n, m = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
#
# for i in sorted(a+b):
#     print(i, end=" ")

# 다른 풀이 (아래 풀이가 속도는 더 느림)

a_idx, b_idx = 0, 0
c = []
while a_idx < n and b_idx < m:

    if a[a_idx] < b[b_idx]:
        c.append(a[a_idx])
        a_idx += 1
    else:
        c.append(b[b_idx])
        b_idx += 1

if a_idx != n:
    c.extend(a[a_idx:])
if b_idx != m:
    c.extend(b[b_idx:])

for i in c:
    print(i, end=" ")