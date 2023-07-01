import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
nums = list(map(int, input().split()))

nums.sort()
s, e = 0, N - 1
cnt = 0

while s < e:
    temp = nums[s] + nums[e]
    if temp == M:
        cnt += 1
        s += 1
        e -= 1
    elif temp > M:
        e -= 1
    elif temp < M:
        s += 1

print(cnt)
