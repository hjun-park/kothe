import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
s = [0] * (N + 1)

# 1. 구간 합 계산하기
for i in range(1, N + 1):
    s[i] = s[i - 1] + nums[i - 1]

# 2. 구간 합 구하기
for _ in range(M):
    a, b = map(int, input().split())
    print(s[b] - s[a - 1])
