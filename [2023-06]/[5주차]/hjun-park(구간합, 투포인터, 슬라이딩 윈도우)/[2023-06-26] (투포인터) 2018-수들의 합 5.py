import sys

input = sys.stdin.readline

N = int(input().rstrip())
left = right = 1

cnt = 1
_sum = 1
while right != N:
    if _sum == N:
        cnt += 1
        right += 1
        _sum += right
    elif _sum > N:
        _sum -= left
        left += 1
    elif _sum < N:
        right += 1
        _sum += right

print(cnt)
