import sys
from collections import deque

input = sys.stdin.readline


N = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(N)]

rst = 0
plus_q = deque()
minus_q = deque()
zero = 0
one = 0

nums.sort(reverse=True)

for n in nums:
    if n == 1:
        one += 1
    elif n == 0:
        zero += 1
    elif n > 1:
        plus_q.append(n)
    elif n < 0:
        minus_q.append(n)

while len(plus_q) > 1:
    a = plus_q.popleft()
    b = plus_q.popleft()

    rst += (a * b)

if plus_q:
    r = plus_q.popleft()
    rst += r

rst += one

while len(minus_q) > 1:
    a = minus_q.pop()
    b = minus_q.pop()

    rst += (a * b)

if minus_q and zero == 0:
    r = minus_q.pop()
    rst += r

print(rst)
